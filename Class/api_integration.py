import requests
from config import API_KEY,URL
headers = {
    "x-goog-api-key" :  API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    "contents":[
        {
            "parts":[
                {"text":"Explain api testing in simple terms"}
            ]
        }
    ]
}

response = requests.post(URL, headers=headers,json=payload)
print("status code:", response.status_code)
data = response.json()
print(data)

if "candidates" in data:
    print(data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("no candidates found")


