from Google_API.google_api_authentication_client import refresh_token_service_object
import json
import pandas as pd


def gtm_account_details():

    tagmanager_service = refresh_token_service_object("tagmanager", "v2","/Work/python_projects/GTM_API/client_secret_akdm.json",
                             "/Work/python_projects/GTM_API/refresh_token.txt")

    account_details = tagmanager_service.accounts().list().execute()

    print(account_details)

    account_details_df = pd.DataFrame(account_details['account'])
    account_details_df.to_excel("/Work/python_projects/GTM_API/gtm_details.xlsx",sheet_name='Accounts')

    container_details = []

    for path in account_details_df['path']:

        account_details_containers = tagmanager_service.accounts().containers().list(parent=path).execute()
        container_details.append(account_details_containers)

    # for container in container_details:
    #
    # container_details_df = pd.DataFrame(container)
    # print(container_details_df)
    #4004
    # container_details_df.to_excel("/Work/python_projects/GTM_API/gtm_details.xlsx",sheet_name='Containers')


    # print(account_details_df['accountId'])





gtm_account_details()