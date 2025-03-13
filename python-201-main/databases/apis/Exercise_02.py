'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(base_url)
print(response.status_code)
print(response.encoding)
data = response.json()

def get_emails(api_response):
    emails = []
    for item in api_response['data']:
        emails.append(item["email"])
    return emails

print(get_emails(data))
    