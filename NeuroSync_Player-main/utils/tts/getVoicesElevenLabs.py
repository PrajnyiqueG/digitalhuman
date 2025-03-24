import requests

XI_API_KEY = "sk_49bac64baa8fe562d8eb788ec3873f20de12b2b4353badac"

url = "https://api.elevenlabs.io/v1/voices"

headers = {"Accept": "application/json","xi-api-key": XI_API_KEY,"Content-Type": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

for voice in data['voices']:
	print(f"{voice['name']}; {voice['voice_id']}")
	
# Keep the window open
input("Press Enter to exit...")
