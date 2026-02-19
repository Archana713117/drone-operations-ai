import gspread
import pandas as pd
import json
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def get_creds():
    # running on streamlit cloud
    if "gcp" in st.secrets:
        creds_dict = dict(st.secrets["gcp"])
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    else:
        # running locally
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

    return creds

def load_sheet(sheet_name):
    client = gspread.authorize(get_creds())
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)
