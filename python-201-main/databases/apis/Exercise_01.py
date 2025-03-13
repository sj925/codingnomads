'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''
import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

status_code = requests.get(base_url)
print(status_code)
encoding = requests.get(base_url).encoding
print(encoding)
body = requests.get(base_url).json()
pprint(body)