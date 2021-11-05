from googleapiclient.discovery import build
from google.oauth2 import service_account
from exchange_rates_fixed import cur, exc_rat
import os
import sys
import pandas as pd
import webbrowser



def spreadsheet_w_f():


    SERVICE_ACCOUNT_FILE = os.path.join(sys.path[0], "keys.json")
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1kOaQAhonJzYo7weurSmiaYiR8B_J1iqwnckPAuJMCJU'

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    results = service.spreadsheets().values().batchUpdate(spreadsheetId = SAMPLE_SPREADSHEET_ID, body = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "exchange rates for 2010-01-15!B1",
             "majorDimension": "COLUMNS",
             "values":[exc_rat] },
            {"range": "exchange rates for 2010-01-15!A1",
             "majorDimension": "COLUMNS",
             "values":[cur] }
        ]
    }).execute()


def spreadsheet_r_f():


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


def spreadsheet_d_f():


    SERVICE_ACCOUNT_FILE = os.path.join(sys.path[0], "keys.json")
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1kOaQAhonJzYo7weurSmiaYiR8B_J1iqwnckPAuJMCJU'

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    deleting = service.spreadsheets().values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                     range="exchange rates for 2010-01-15!A1:B154").execute()


def html_fixed():


    df = pd.DataFrame(exc_rat, cur)


    html = df.to_html(header=False)

    text_file = open("exchange_rates_for_2010-01-15.html", "w")
    text_file.write(html)
    text_file.close()

    webbrowser.open_new_tab('exchange_rates_for_2010-01-15.html')