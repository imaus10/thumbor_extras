# thumbor_extras

Some useful extensions to thumbor.

## Detectors

### dnn_face_detector

An improved face detector that uses a deep neural network. More specifically, it uses the [SSD object detection model](https://arxiv.org/abs/1512.02325), trained specifically on faces. According to [this](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/how_to_train_face_detector.txt), it was trained with "some huge and available online dataset." :/

For more information on how the normal thumbor face detector compares to this one, see [this repo](https://github.com/imaus10/compare_face_detection).

### dnn_object_detector

The full SSD object detection model, trained on the [COCO dataset](http://cocodataset.org). It was built as a [MobileNet](https://arxiv.org/abs/1704.04861), a class of efficient, light weight deep neural network models meant to work well in mobile and embedded applications.

## Filters

### draw_focal_points

Draws a box around the focal points, for displaying the results of the detectors on a given image.

## TODO

- Make it pip-install-able
- Choose thresholds empirically
