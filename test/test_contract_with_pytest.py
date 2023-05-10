import pytest
from specmatic_python.server.flask_server import FlaskServer
from specmatic_python.specmatic.specmatic_server import SpecmaticServer
from api import app
from definitions import ROOT_DIR

host = "127.0.0.1"
port = 5000
flask_server = FlaskServer(app, host, port)


class TestContract:

    @classmethod
    def teardown_class(cls):
        flask_server.stop()


flask_server.start()
SpecmaticServer() \
    .with_api_under_test_at(host, port) \
    .with_specmatic_json_at(ROOT_DIR + '/specmatic.json') \
    .configure_py_tests(TestContract)

if __name__ == '__main__':
    pytest.main()
