import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook/ca402f54-1679-474d-b5c6-f2e309659f09"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])