import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/members/364388bc-5b7f-4857-a58c-31eba18e962e"

payload = ""
headers = {
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", url, data=payload, 
headers=headers)

print(response.text)
