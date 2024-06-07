import os

import pytest
from specmatic.core.specmatic import Specmatic

from api import app
from definitions import ROOT_DIR

os.environ["SPECMATIC_GENERATIVE_TESTS"] = "true"


class TestContract:
    pass


Specmatic().with_project_root(ROOT_DIR).with_wsgi_app(app).test_with_api_coverage_for_flask_app(TestContract, app).run()

if __name__ == "__main__":
    pytest.main()
