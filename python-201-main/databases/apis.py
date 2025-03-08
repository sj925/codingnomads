import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
user_id = 10448
specific_user_url = f"{base_url}/{user_id}"
response = requests.get(specific_user_url)
pprint(f"initial response: {response.json()}\n")
body = {
    "first_name" : "Marko",
    "last_name" : "Dingus",
    "email" : "bigdawg@aol.com"
}
response = requests.put(specific_user_url, json=body)
print(f"Request Response: {response.status_code}\n")
response = requests.get(specific_user_url)
pprint(f"response update: {response.json()}")

response = requests.delete(specific_user_url)
print(response.status_code)



