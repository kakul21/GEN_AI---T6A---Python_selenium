import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

## Register API Call

def reg_post():
    response = requests.post('https://www.shoppersstack.com/shopping/shoppers', json=payload, verify=False)
    return response.json()

reg_post()

## login details
login_data={
  "email": "kakul45@gmail.com",
  "password": "Password4",
  "role": "SHOPPER"
}

##Login API Call

def login_post():
    response1 = requests.post('https://www.shoppersstack.com/shopping/users/login', json=login_data, verify=False)
    return response1.json()

## Extract Authentication Data

login_res = login_post()
print(login_res)
data = login_res['data']
userid = data['userId']
token = data['jwtToken']
print(token)

## Authorized GET Request
def authorize_get():
    header = {'Authorization': f"Bearer {token}"}
    response = requests.get(f'https://www.shoppersstack.com/shopping/shoppers/{userid}', headers=header,verify=False)
    return response.status_code

print(authorize_get())