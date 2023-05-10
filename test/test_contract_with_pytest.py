import pytest
from specmatic_python.specmatic.specmatic_server import SpecmaticServer
from definitions import ROOT_DIR

host = "127.0.0.1"
port = 5000


class TestContract:
    pass


SpecmaticServer() \
    .with_api_under_test_at(host, port) \
    .with_specmatic_json_at(ROOT_DIR + '/specmatic.json') \
    .configure_py_tests(TestContract)

if __name__ == '__main__':
    pytest.main()
