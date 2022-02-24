import gspread
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('covid_data')

"""
record = SHEET.worksheet('Record_Covid_Case')

data = record.get_all_values()
"""

def get_record_data():
    """
    Record covid data from the user
    """
    print("Please record covid cases from todays date")
    print("The following headings must be updated\n")
    print("Date, CovidConfirmed, Hopitalised, Male, Female, TotalDeaths")
    print("Example: 04/02/2022,1,0,0,1,0\n")

    data_str = input("Enter your data here:")

    record_data = data_str.split(",")
    validate_data(record_data)

def validate_data(values):
    """
    all values to integers
    presents error if cannot convert string to integers
    looks for exactly 6 inputs with the first input a date
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        
    print(values)


get_record_data()