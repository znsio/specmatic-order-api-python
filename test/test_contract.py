import pytest
from specmatic.core.specmatic import Specmatic

from api import app
from definitions import ROOT_DIR


class TestContract:
    pass


Specmatic() \
    .with_project_root(ROOT_DIR) \
    .with_wsgi_app(app) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
