import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication
import requests
import json

#SCOPES = ['User.Read.All']
SCOPES = ["https://graph.microsoft.com/.default"]

# The App Registration's application (client) ID
client_id = '12981ac8-3f9b-48b0-9839-918ecebbca70'

# Your Azure AD tenant ID
tenant_id = 'ea7b03ca-00db-4c19-9b8c-6442ab16a46f'

ENDPOINT_URI = 'https://graph.microsoft.com/beta/'

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


def listAllConfigs():
    request = requests.get(url=ENDPOINT_URI+'/deviceManagement/configurationPolicies', headers=req_headers)
    print(request)
    print(json.dumps(request.json(), indent=5, ensure_ascii=False))


def get_specific_config(config_id):
    request = requests.get(url=ENDPOINT_URI+f'/deviceManagement/configurationPolicies/{config_id}', headers=req_headers)
    return request.json()

def get_specific_config_settings(config_id):
    request = requests.get(url=ENDPOINT_URI+f'/deviceManagement/configurationPolicies/{config_id}/settings', headers=req_headers)
    #print(request)
    #print(json.dumps(request.json(), indent=5, ensure_ascii=False))
    return request.json()


def create_specific_config(json):
    request = requests.post(url=ENDPOINT_URI+f'/deviceManagement/configurationPolicies/', headers=req_headers, json=json)
    print(request.json())

test_json = {
     "@odata.context": "https://graph.microsoft.com/beta/$metadata#deviceManagement/configurationPolicies/$entity",
     "createdDateTime": "2023-03-28T12:13:13.4842787Z",
     "creationSource": 'null',
     "description": "",
     "lastModifiedDateTime": "2023-03-28T12:13:13.4842787Z",
     "name": "test2",
     "platforms": "windows10",
     "priorityMetaData": None,
     "roleScopeTagIds": [
          "0"
     ],
     "settingCount": 2,
     "technologies": "mdm",
     "id": "b553a081-4cce-4ef9-bda5-8f2df5172ca8",
     "templateReference": {
          "templateId": "",
          "templateFamily": "none",
          "templateDisplayName": 'null',
          "templateDisplayVersion": 'null'
     },
"settings":  [
                     {
                         "id":  "0",
                         "settingInstance":  {
                                                 "@odata.type":  "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance",
                                                 "settingDefinitionId":  "user_vendor_msft_policy_config_admx_controlpaneldisplay_cpl_personalization_enablescreensaver",
                                                 "settingInstanceTemplateReference":  None,
                                                 "choiceSettingValue":  {
                                                                            "settingValueTemplateReference":  None,
                                                                            "value":  "user_vendor_msft_policy_config_admx_controlpaneldisplay_cpl_personalization_enablescreensaver_1",
                                                                            "children":  [

                                                                                         ]
                                                                        }
                                             }
                     },
                     {
                         "id":  "1",
                         "settingInstance":  {
                                                 "@odata.type":  "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance",
                                                 "settingDefinitionId":  "user_vendor_msft_policy_config_admx_controlpaneldisplay_cpl_personalization_screensaverissecure",
                                                 "settingInstanceTemplateReference":  None,
                                                 "choiceSettingValue":  {
                                                                            "settingValueTemplateReference":  None,
                                                                            "value":  "user_vendor_msft_policy_config_admx_controlpaneldisplay_cpl_personalization_screensaverissecure_1",
                                                                            "children":  [

                                                                                         ]
                                                                        }
                                             }
                     }
                 ]
}

config_id = '3bd139ed-66b3-4afc-975c-dc81eae1f2b8'
#createNewUser(user_json)
#listAllUsers()
#listAllConfigs()
policy_json = get_specific_config(config_id)
policy_json_settings = get_specific_config_settings(config_id)['value']
print(json.dumps(policy_json, indent=5, ensure_ascii=False))
print(json.dumps(policy_json_settings, indent=5, ensure_ascii=False))

policy_json['settings'] = policy_json_settings
policy_json['name'] = 'new_awsome_name'
print(json.dumps(policy_json,indent=10,ensure_ascii=False))


#print(merged_json)
create_specific_config(policy_json)

