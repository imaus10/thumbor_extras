import pytest
from thumbor_extras.detectors.dnn_face_detector import Detector

@pytest.mark.parametrize('image_context_arg', [
    'face_image_context', 'gray_face_image_context', 'cmyk_face_image_context'
])
def test_should_detect_one_face(image_context_arg, request):
    image_context = request.getfixturevalue(image_context_arg)
    Detector(image_context, 0, None).detect(lambda: None)
    detections = image_context.request.focal_points
    assert len(detections) == 1
