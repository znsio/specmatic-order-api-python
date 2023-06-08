import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer

from definitions import ROOT_DIR

from api import app


class TestContract:
    pass


app_server = WSGIAppServer(app)
Specmatic() \
    .with_project_root(ROOT_DIR) \
    .app(app_server) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
