import pytest
from specmatic.core.decorators import start_flask_app, specmatic_contract_test
from api import app

host = "127.0.0.1"
port = 5000


@specmatic_contract_test(host, port)
@start_flask_app(app, host, port)
class TestContract:
    @classmethod
    def teardown_class(cls):
        cls.flask_server.stop()




if __name__ == '__main__':
    pytest.main()
