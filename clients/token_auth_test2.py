import requests
from pprint import pprint

def client():
    token = "Token cce6b1e0203469af713376ea32fa63f3f4a32612"

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url = 'http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers= headers,
    )

    print('Status Code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()