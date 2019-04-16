# thumbor_extras

Some useful extensions to thumbor.

Currently not yet a pip package, so to use, you must `git clone` and add the root dir to your `PYTHONPATH`:

```
export PYTHONPATH=$PYTHONPATH:/path/to/thumbor_extras
```

## Detectors

Add these detectors to your `thumbor.conf`:

```
DETECTORS = [
    'thumbor_extras.detectors.dnn_face_detector',
    'thumbor_extras.detectors.dnn_object_detector'
]
```

### dnn_face_detector

An improved face detector that uses a deep neural network. More specifically, it uses the [SSD object detection model](https://arxiv.org/abs/1512.02325), trained specifically on faces. According to [the OpenCV repo](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/how_to_train_face_detector.txt), it was trained with "some huge and available online dataset." :/

For more information on how the normal thumbor face detector compares to this one in both accuracy and efficiency, see [this comparison script](https://github.com/imaus10/compare_face_detection).

### dnn_object_detector

The full SSD object detection model, trained on the [COCO dataset](http://cocodataset.org). It was built as a [MobileNet](https://arxiv.org/abs/1704.04861), a class of efficient, light weight deep neural network models meant to work well in mobile and embedded applications.

## Filters

Add these filters to your available filters in `thumbor.conf`:

```
FILTERS = [
    ...other filters,
    'thumbor_extras.filters.draw_focal_points'
]
```

### draw_focal_points

Draws a box around the focal points, for displaying the results of the detectors on a given image. Takes optional arguments for box color and line width.

Usage: `draw_focal_points([r, g, b, line_width])`

Examples:
- `draw_focal_points()`: draws boxes with defaults (green color and 3 pixel line width).
- `draw_focal_points(255,0,0,5)`: draws boxes with red color and 5 pixel line width.

Arguments:

- `r`: R component of RGB color of box, default 0
- `g`: G component of RGB color of box, default 255
- `b`: B component of RGB color of box, default 0
- `line_width`: the width of the box lines

## TODO

- Make it pip-install-able
- Choose thresholds empirically
