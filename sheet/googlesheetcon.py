import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Administrator\\Desktop\\anth\\.env\\sheet\\api_logs\\sheet_credentials.json", scopes = scope)
file = gspread.authorize(creds)
workbook = file.open("Students")
worksheet = workbook.get_worksheet(0)
sheet = worksheet.get_all_values()

print("PERFECT TEAM WORK NEED GOOD INPUT")

# Print all files
for rows in sheet:
    print(rows)
    # for name in rows:
    #     print(name)