# Google API Authentication for Installed Applications

#### This repo has python script to authenticate google API for Installed applications using oAuth 2.0 to generate tokens for making API requests to various Google API. The file has GoogleAuthentication class and methods to do the needfull and can be used with any Google API for automation of tasks, reporting automation and other usecases.

|          Dependencies          |   
| ------------------------------ |
| google_auth_oauthlib==0.2.0    |
| protobuf==3.6.0                | 
| google_api_python_client==1.7.3|

### Table of Contents
**[Installation and Usage Instructions](#installation-and-usage-instructions)**<br>
**[Methods and objects](#methods-and-objects)**<br>
**[Example](#example)**<br>



## Installation and Usage Instructions

1. Clone this repo.
2. Add this directory to [sys.path](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)
3. Create [Google Developer Console](console.cloud.google.com) Project
4. Activate the required API
5. Generate API OAuth 2.0 keys
6. create instance of GoogleAuthentication class, with required inputs as stated below
7. Description and usage of each class method is given below

## Methods and objects

|     parameters            |           Description           |
| ------------------------- |:-------------------------------:|
| api_name, api_version | name and version of the API in [google documentation](https://developers.google.com/api-client-library/python/apis/)|
| scope     | Scopes of [API](https://developers.google.com/identity/protocols/googlescopes) that needs to be authenticated.| 
| credentials_directory   | directory where client_secrests from API console are stored| 
| client_secret_json      | client secret JSON file |

#### google_authorization_access()
      
This method can be invoked on the instance of GoogleAuthentication class to autheticate access to the API and generate tokens for API queries. It returns a service object and can be used for temporary period only untill the access token expire. It also generate a refresh token file in the same directory that can leveraged in refresh_token_service_object() method.
      
      
#### refresh_token_service_object(refresh_token_file)

This method can be invoked on the instance of GoogleAuthentication class to leverage the refersh tokens generated using the google_authorization_access() method. It takes refresh token file name as parameter. This method also generates an service object which can be used to make API queries using refresh token(no expiration).

#### Example
      scope = ['https://www.googleapis.com/auth/tagmanager.readonly',
                 'https://www.googleapis.com/auth/tagmanager.edit.containers',
                 'https://www.googleapis.com/auth/tagmanager.delete.containers',
                 'https://www.googleapis.com/auth/tagmanager.edit.containerversions',
                 'https://www.googleapis.com/auth/tagmanager.publish',
                 'https://www.googleapis.com/auth/tagmanager.publish',
                 'https://www.googleapis.com/auth/tagmanager.manage.users',
                 'https://www.googleapis.com/auth/tagmanager.manage.accounts'
                 ]
      Google_tag_manager = GoogleAuthentication("tagmanager","v2", scope, credentials_directory_path, client_secret_json_file)
      
  For first time and temporary API queries
      
      service = Google_tag_manager.google_authorization_access()
      account_details = service.accounts().list().execute()
      print(account_details)
      
  For using the access tokens and not avoid authentication
      
      service = Google_tag_manager.refresh_token_service_object(refresh_token_file_path)
      account_details = service.accounts().list().execute()
      print(account_details)
      
      
