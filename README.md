This is a Python implementation of the [Specmatic Order API](https://github.com/znsio/specmatic-order-api) project.  
The implementation is based on [Python Flask](https://flask.palletsprojects.com/en/2.3.x/)

The open api contract for the services is defined in the [Specmatic Central Contract Repository](https://github.com/znsio/specmatic-order-contracts/blob/main/in/specmatic/examples/store/api_order_v1.yaml)


```Dev Setup```

- Install Python 3.11 ( use homebrew if you are on mac os)
- Install pip
- Install virtualenv by running:  
  ```pip install virtualenv```

- Clone the git repository

- **Virtual Environment Setup** 
  - Create a "virtual environment" named 'venv' by running:  
    ```virtualenv venv ```  

      This will create a virtual environment using the default python installation.  
      If you wish to provide a specific python installation, run:  
    ```virtualenv venv --python="/opt/homebrew/Cellar/python@3.11/3.11.3/libexec/bin/python"```  

  - To activate your virtual environment, execute this from a terminal window in your root folder:  
    ```source venv/bin/activate```  

- **Install project requirements**  
    From a terminal window in your root folder, run:  
    ``` pip install -r requirements.txt```  
    Reload the virtual env:  
    ```deactivate```   
    ```source venv/bin/activate```   

- **Start the Flask app**  
  From a terminal window in your root folder, run:
  ```flask run```  
  This should start the flask dev server on http://127.0.0.1:5000/
  
  To check, run this route from postman:
  ```http://127.0.0.1:5000/products/10```

  You should see a response like this:
    ``` `{
    "id": 10,
    "inventory": 10,
    "name": "XYZ Phone",
    "type": "gadget"
    } ```   

- **Validate contract using Specmatic**  
  With the flask api server running on ```http://127.0.0.1:5000/```, open another terminal window in the root folder and run:  
  ```specmatic test  --host="127.0.0.1" --port=5000```  
  This should print the following output:  
  
    |------------------------------------------------------|  
    | API COVERAGE SUMMARY                                 |  
    |------------------------------------------------------|  
    |  status |           path | method | response | count |  
    |---------|----------------|--------|----------|-------|  
    | covered |        /orders |    GET |      200 |     1 |  
    |         |                |   POST |      200 |     1 |  
    | covered |   /orders/{id} | DELETE |      200 |     1 |  
    |         |                |    GET |      200 |     1 |  
    |         |                |        |      404 |     1 |  
    |         |                |   POST |      200 |     1 |  
    | covered |      /products |    GET |      200 |     2 |  
    |         |                |        |      500 |     1 |  
    |         |                |   POST |      200 |     1 |  
    | covered | /products/{id} | DELETE |      200 |     1 |  
    |         |                |    GET |      200 |     1 |  
    |         |                |        |      404 |     1 |  
    |         |                |   POST |      200 |     1 |  
    |------------------------------------------------------|  
    | 4 / 4 APIs covered                                   |  
    |------------------------------------------------------|  
    Tests run: 14, Successes: 14, Failures: 0, Errors: 0  
    
 