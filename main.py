import webbrowser
import msal
import requests
import json

SCOPES = ['User.Read.All']

# The App Registration's application (client) ID
client_id = '12981ac8-3f9b-48b0-9839-918ecebbca70'

# Client secret created under App Registration blade
client_secret = 'e_r8Q~Maz-egB~Eq5uKAhEh4qzZc1sF-88yNqaWo'

# Your Azure AD tenant ID
tenant_id = 'ea7b03ca-00db-4c19-9b8c-6442ab16a46f'

app = msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}")

scopes = ["https://graph.microsoft.com/.default"]

ENDPOINT_URI = 'https://graph.microsoft.com/v1.0/'

user_json = {
    "accountEnabled": 'true',
    "displayName": "Testowy2 test",
    "mailNickname": "Testowy2Test",
    "userPrincipalName": "Testowy2Test@2xy2fl.onmicrosoft.com",
    "passwordProfile" : {
        "forceChangePasswordNextSignIn": 'true',
        "password": "xWwvJ]6NMw+bWH-d"
    }
}




# Obtain bearer token from MS Graph
token = None
token = app.acquire_token_for_client(scopes=scopes)
#token = app.acquire_token_by_refresh_token(scopes=scopes, refresh_token=token['access_token'])

print(token)

req_headers = {
    "Authorization": "Bearer " + token['access_token'],
    "Content-Type": "application/json"
}

#response = requests.get(url=ENDPOINT_URI+'users', headers=req_headers)

#print(response)
#print(json.dumps(response.json(), indent=5, ensure_ascii=False))


def getAllUsers():
    response = requests.get(url=ENDPOINT_URI+'users', headers=req_headers)
    print(response)
    print(json.dumps(response.json(), indent=5, ensure_ascii=False))


def createNewUser(json):
    request = requests.post(url=ENDPOINT_URI+'users', headers=req_headers, json=json)
    print(request.status_code)
    print(request.json())


createNewUser(user_json)
