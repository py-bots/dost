from excel import authenticate_google_spreadsheet,excel_get_dataframe_from_google_spreadsheet

url="https://docs.google.com/spreadsheets/d/1z5h839kECYR484hPBYR-mC_hkxXkmuJjU-5wOoj78BQ"
auth=authenticate_google_spreadsheet("D:\Pybots resources\Excel\cred.json")
df=excel_get_dataframe_from_google_spreadsheet(auth,spreadsheet_url=url, sheet_name="Sheet1")
print(df)