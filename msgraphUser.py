import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication
import requests
import json

#SCOPES = ['User.Read.All']
SCOPES = ["https://graph.microsoft.com/.default"]

upn='suadmin@2xy2fl.onmicrosoft.com'
password='iKKRPXFaPthQh7D'

# The App Registration's application (client) ID
client_id = '12981ac8-3f9b-48b0-9839-918ecebbca70'

# Client secret created under App Registration blade
client_secret = 'e_r8Q~Maz-egB~Eq5uKAhEh4qzZc1sF-88yNqaWo'

# Your Azure AD tenant ID
tenant_id = 'ea7b03ca-00db-4c19-9b8c-6442ab16a46f'

ENDPOINT_URI = 'https://graph.microsoft.com/v1.0/'

app = PublicClientApplication(
    client_id=client_id,
    authority=f"https://login.microsoftonline.com/{tenant_id}")


acquire_tokens_result = app.acquire_token_interactive(scopes=SCOPES)

print(acquire_tokens_result)

'''
if 'error' in acquire_tokens_result:
  print("Error: " + acquire_tokens_result['error'])
  print("Description: " + acquire_tokens_result['error_description'])
else:
  print("Access token:\n")
  print(acquire_tokens_result['access_token'])
  print("\nRefresh token:\n")
  print(acquire_tokens_result['refresh_token'])

'''

req_headers = {
    "Authorization": "Bearer " + acquire_tokens_result['access_token'],
    "Content-Type": "application/json"
}


user_json = {
  "accountEnabled": 'true',
  "displayName": "Testowy test",
  "mailNickname": "TestowyTest",
  "userPrincipalName": "TestowyTest@2xy2fl.onmicrosoft.com",
  "passwordProfile" : {
    "forceChangePasswordNextSignIn": 'true',
    "password": "xWwvJ]6NMw+bWH-d"
  }
}

def getAllUsers():
    response = requests.get(url=ENDPOINT_URI+'users', headers=req_headers)
    print(response)
    print(json.dumps(response.json(), indent=5, ensure_ascii=False))


def listAllUsers():
    request = requests.get(url=ENDPOINT_URI+'groups', headers=req_headers)
    print(request)
    print(json.dumps(request.json(), indent=5, ensure_ascii=False))


def createNewUser(json):
    request = requests.post(url=ENDPOINT_URI+'users', headers=req_headers, json=json)
    print(request.status_code)
    print(request.json())


#createNewUser(user_json)
listAllUsers()
