import cv2
import numpy as np
import os
from thumbor.detectors import BaseDetector
from thumbor.point import FocalPoint
from thumbor.utils import logger

class Detector(BaseDetector):
    def __init__(self, context, index, detectors):
        super(Detector, self).__init__(context, index, detectors)
        this_dir = os.path.dirname(os.path.abspath(__file__))
        self.net = cv2.dnn.readNet(
            os.path.join(this_dir, 'frozen_inference_graph.pb'),
            os.path.join(this_dir, 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
        )

    def detect(self, callback):
        engine = self.context.modules.engine
        try:
            img_data = engine.image
            img = np.array(engine.image)
            self.net.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True))
            faces = self.net.forward()
        except Exception as e:
            logger.exception(e)
            logger.warn('Error during feature detection; skipping to next detector')
            self.next(callback)
            return

        # TODO: choose a threshold value based on empirical evidence
        confidence_threshold = 0.2
        num_faces = faces.shape[2]
        if num_faces > 0:
            for i in range(num_faces):
                confidence = float(faces[0, 0, i, 2])
                if confidence < confidence_threshold:
                    continue
                left = int(faces[0, 0, i, 3] * img.shape[1])
                top = int(faces[0, 0, i, 4] * img.shape[0])
                right = int(faces[0, 0, i, 5] * img.shape[1])
                bottom = int(faces[0, 0, i, 6] * img.shape[0])
                width = right - left
                height = bottom - top
                self.context.request.focal_points.append(
                    FocalPoint.from_square(left, top, width, height, origin="DNN Object Detection")
                )
            callback()
        else:
            self.next(callback())
