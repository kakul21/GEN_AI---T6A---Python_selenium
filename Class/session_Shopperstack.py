import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://www.shoppersstack.com/shopping"

## user details
payload = {
    "city": "jaipur",
    "country": "india",
    "email": "kakul45@gmail.com",
    "firstName": "Kakul",
    "gender": "FEMALE",
    "lastName": "Jain",
    "password": "Password4",
    "phone": 8567941840,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
}

## login details

login_data = {
    "email": "kakul45@gmail.com",
    "password": "Password4",
    "role": "SHOPPER"
}


session = requests.Session()
session.verify = False
def reg_post():
    response = session.post(f"{BASE_URL}/shoppers", json=payload)
    return response.json()

def login_post():
    response = session.post(f"{BASE_URL}/users/login", json=login_data)
    return response.json()

def get_user(userid):
    response = session.get(f"{BASE_URL}/shoppers/{userid}")
    return response.status_code, response.json()

## User Authentication (Login)

reg_post()
login_response = login_post()
print(login_response)

data = login_response['data']
userid = data['userId']
token = data['jwtToken']

# Session Becomes Authenticated
session.headers.update({
    "Authorization": f"Bearer {token}"
})

# Fetch User Data
status, user_data = get_user(userid)

print(status)
print(user_data)




