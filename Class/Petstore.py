import requests

## GET
'''response = requests.get("https://petstore.swagger.io/v2/store/inventory")
print(response.text)
print(response.status_code)
print(response.json())

response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
print(response.status_code)
print(response.text)'''

## Fetch any value through keys
'''response = requests.get("https://petstore.swagger.io/v2/pet/1")
print(response.text)
print(response.status_code)
print(response.json())
dict = response.json()
print(dict['name'])
print(dict['tags'])
print(dict['category'])
print(dict['status'])'''

## POST
'''data1={
  "id": 100,
  "category": {
    "id": 0,
    "name": "Animal"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tag1"
    }
  ],
  "status": "available"
}

response = requests.post("https://petstore.swagger.io/v2/pet",json=data1)
print(response.json())
print(response.status_code)
assert response.status_code == 200'''

## DELETE
'''response = requests.delete("https://petstore.swagger.io/v2/pet/3")
print(response.status_code)'''

## PUT
'''data={
  "id": 100,
  "category": {
    "id": 0,
    "name": "animal"
  },
  "name": "ABC",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.put("https://petstore.swagger.io/v2/pet",json=data)
print(response.status_code)
print(response.json())

response = requests.get("https://petstore.swagger.io/v2/pet/100")
print(response.status_code)
print(response.json())'''

## Create three functions to perform post,get,delete

'''def post(url):
    data={
  "id": 100,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
    response = requests.post(url,json=data)
    Id = response.json()["id"]
    return Id

def get(id_name):
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{id_name}")
    print(response.status_code)

def delete(id_name):
    response= requests.delete(f"https://petstore.swagger.io/v2/pet/{id_name}")
    print(response.status_code)

id_name = post("https://petstore.swagger.io/v2/pet")
get(id_name)
delete(id_name)'''






