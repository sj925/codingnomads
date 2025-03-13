'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

def create_user(url:str, user_data:dict) -> str:
    """
    Try to create a user, handling cases where user might already exist
    """
    try:
        get_response = requests.get(url)
        existing_users = get_response.json()['data']
        
        for user in existing_users:
            if user['email'] == user_data['email']:
                return f"User with email {user_data['email']} already exists!"
            
        post_response = requests.post(url, json=user_data)
        
        if post_response.status_code == 201:
            return f"User created successfully: {post_response.json()}"
        else:
            return f"Error creating user: {post_response.status_code}"
            
    except requests.RequestException as e:
        return f"Request error: {e}"
    except KeyError as e:
        return f"Data parsing error: {e}"

body = {
    "first_name": "epeez",
    "last_name": "vale",
    "email": "hotdawg@aol.com"
}

result = create_user(base_url, body)
print(result)
    