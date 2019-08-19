import pytest
from thumbor_extras.detectors.tests.helpers import github_image_fixture

@pytest.fixture
def face_image_context():
    return github_image_fixture('Giunchedi%252C_Filippo_January_2015_01.jpg')

@pytest.fixture
def gray_face_image_context():
    return github_image_fixture('Giunchedi%252C_Filippo_January_2015_01-grayscale.jpg')

@pytest.fixture
def cmyk_face_image_context():
    return github_image_fixture('Giunchedi%252C_Filippo_January_2015_01-cmyk.jpg')
