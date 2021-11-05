def spreadsheet_r_f():

    from googleapiclient.discovery import build
    from google.oauth2 import service_account
    import os
    import sys

    SERVICE_ACCOUNT_FILE = os.path.join(sys.path[0], "keys.json")
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1kOaQAhonJzYo7weurSmiaYiR8B_J1iqwnckPAuJMCJU'

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="exchange rates for 2010-01-15!A1:B154").execute()
    values = result.get('values', [])
    print(values)
