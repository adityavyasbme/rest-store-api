# REST APIs with python

## Rest API?
- way of thinking about how a web server responds to your server
- it doesn’t respond with just data
- it responds with resources
- think of server of having resources , each is able to interact with pertinent request
- REST is __STATELESS__ : This means one request cannot depend on any other requests


GET - used to send data back only

POST - used to receive data

PUT - post it if not there else update

DELETE - deletes the data
 
- You can use POSTMAN for API Testing
- Flask-JWT - Json web token - used for obfuscation of data, i.e., we can encrypt data. 
- the payload  is the content of JWT token
- JWT create an endpoint; that endpoint is __/auth__  and we send it username and password; JWT authenticates the function and return JWT token and it can be used for further requests.


###Important Commands
'''

Create a venv : virtualenv venv --python=python3.7

Create a safe string comparison on all python version: 

from werkzeug.security import safe_str_cmp


'''
 