# This is a Python implementation of the [Secmatic Order API](https://github.com/znsio/specmatic-order-api) project

## The implementation is based on [Python Flask](https://flask.palletsprojects.com/en/3.0.x/)

The open api contract for the services is defined in the [Specmatic Central Contract Repository](https://github.com/znsio/specmatic-order-contracts/blob/main/in/specmatic/examples/store/api_order_v3.yaml)

### `Dev Setup`

- Install Python 3.12 ( use homebrew if you are on mac os)

- Install JRE 17 or later

- Clone the git repository

- **Virtual Environment Setup**

- Create a "virtual environment" named '.venv' by running:

  - ```shell
    python -m venv .venv
    ```

- This will create a virtual environment using the default python installation, If you wish to provide a specific python installation, run:

  - ```shell
    py -X.Y -m venv .venv
    ```

    where X and Y are the major and minor version numbers of the python installation to use.

- To activate your virtual environment, execute this from a terminal window in your root folder:

  - on MacOS and Linux:

    ```shell
    source .venv/bin/activate
    ```

  - on Windows:
  
    on CMD

    ```cmd
    .venv\Scripts\activate.bat
    ```

    on PowerShell ( might have to change ExecutionPolicy )

    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

- **Install project requirements**

  From a terminal window in your root folder, run:

  ```shell
  pip install -r requirements.txt
  ```

### `Start the Flask app`

- From a terminal window in your root folder, run:

  - ```shell
    flask run
    ```

- This should start the flask dev server on <http://127.0.0.1:5000/>

- To check, run this route from browser:

  - <http://127.0.0.1:5000/products/10>

- You should see a response like this:

    ```json
    {
    "id": 10,
    "inventory": 10,
    "name": "XYZ Phone",
    "type": "gadget"
    }
    ```

### `Validate contract using Specmatic`

- From a terminal window in your root folder, run:

  - ```shell
    pytest test -v -s
    ```

- This should print the following output:
  
  ```cmd
  Tests run: 162, Successes: 162, Failures: 0, Errors: 0
  ```
