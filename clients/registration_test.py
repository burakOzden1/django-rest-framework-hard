import requests
from pprint import pprint

def client():
    credentials = {
        'username': 'rest_test_user4',
        'email': 'test4@test.co',
        'password1': 'testing321..',
        'password2': 'testing321..',
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/dj-rest-auth/registration/',
        data = credentials,
    )

    print('Status Code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()