import mock
import os
import pytest
from thumbor.engines.pil import Engine as PilEngine
# this will break with python3
from urllib import urlretrieve

def github_image_fixture(image_filename):
    return image_fixture(
        'https://raw.githubusercontent.com/thumbor/thumbor/master/tests/fixtures/images/',
        image_filename
    )

def image_fixture(http_path, image_filename):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    fixtures_dir = os.path.join(this_dir, 'test_fixtures')
    if not os.path.exists(fixtures_dir):
        os.mkdir(fixtures_dir)

    image_path = os.path.join(fixtures_dir, image_filename)
    if not os.path.exists(image_path):
        urlretrieve(
            http_path + image_filename,
            image_path
        )

    context = mock.Mock(request=mock.Mock(focal_points=[]))
    engine = PilEngine(context)
    context.modules.engine = engine
    with open(image_path) as f:
        engine.load(f.read(), None)
    return context
