import pytest
from thumbor_extras.detectors.dnn_object_detector import Detector
from thumbor_extras.detectors.tests.helpers import image_fixture

@pytest.mark.parametrize('image_context_arg', [
    'face_image_context', 'gray_face_image_context', 'cmyk_face_image_context'
])
def test_should_detect_one_face(image_context_arg, request):
    image_context = request.getfixturevalue(image_context_arg)
    Detector(image_context, 0, None).detect(lambda: None)
    detections = image_context.request.focal_points
    assert len(detections) == 1

def test_multiple_detections():
    image_context = image_fixture('http://farm3.staticflickr.com/2023/', '2193566397_b2bd16ab76_z.jpg')
    Detector(image_context, 0, None).detect(lambda: None)
    detections = image_context.request.focal_points
    assert len(detections) == 4
