import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

def load_sheet(sheet_name):
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def update_pilot_status(sheet_name, pilot_id, new_status):
    sheet = client.open(sheet_name).sheet1
    records = sheet.get_all_records()

    for i, row in enumerate(records, start=2):
        if str(row["pilot_id"]) == str(pilot_id):
            sheet.update(f"F{i}", new_status)
            return "Updated Successfully"

    return "Pilot not found"
