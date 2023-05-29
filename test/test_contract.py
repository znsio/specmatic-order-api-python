import pytest
from specmatic.core.specmatic import Specmatic
from definitions import ROOT_DIR

from api import app


class TestContract:
    pass


Specmatic.test_wsgi_app(app,
                        TestContract,
                        with_stub=False,
                        project_root=ROOT_DIR)

if __name__ == '__main__':
    pytest.main()
