import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from processing import load_all_products  # Your function to load the combined product data
from google.oauth2.service_account import Credentials

sheet_name = "Quick Commerce Summary"  
gc_json_key_path = "service_account.json" 

# Authenticate
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file(gc_json_key_path, scopes=scopes)
gc = gspread.authorize(creds)

# Try to open existing sheet
try:
    sh = gc.open(sheet_name)
except gspread.SpreadsheetNotFound:
    print(f"Sheet '{sheet_name}' not found. Please create it manually in Google Drive.")
    exit()

# Load data
df = load_all_products()  # Make sure this returns a pandas DataFrame

# Platform-wise export
platforms = df['platform'].unique()
for platform in platforms:
    ws_title = platform  # Each platform gets its own tab
    try:
        try:
            ws = sh.worksheet(ws_title)
            ws.clear()  # Clear old data
        except gspread.WorksheetNotFound:
            ws = sh.add_worksheet(title=ws_title, rows="100", cols="20")
        # Write DataFrame to worksheet
        platform_df = df[df['platform'] == platform]
        set_with_dataframe(ws, platform_df)
        print(f"{platform} data written to sheet '{sheet_name}' in tab '{ws_title}'")
    except Exception as e:
        print(f"Failed to write {platform} data: {e}")

print("All done!")
