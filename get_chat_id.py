import requests

BOT_TOKEN = '8195218120:AAG6fnCkS6I1XCdj06TbDheJJOxE3zXctKU'
  # Replace with your real token
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(URL)
print(response.json())
