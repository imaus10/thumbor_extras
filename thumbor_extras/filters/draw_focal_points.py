import cv2
import numpy as np
from PIL import Image
from thumbor.filters import BaseFilter, filter_method

class Filter(BaseFilter):
    @filter_method(
        BaseFilter.PositiveNonZeroNumber,
        BaseFilter.PositiveNumber,
        BaseFilter.PositiveNumber,
        BaseFilter.PositiveNumber
    )
    def draw_focal_points(self, line_width=3, r=0, g=255, b=0):
        img = np.array(self.engine.image)
        for focal_point in self.context.request.focal_points:
            width = int(focal_point.width)
            height = int(focal_point.height)
            left = int(focal_point.x - (width / 2))
            top = int(focal_point.y - (height / 2))
            right = left + width
            bottom = top + height
            cv2.rectangle(img, (left, top), (right, bottom), (r, g, b), line_width)
            self.engine.image = Image.fromarray(img)
