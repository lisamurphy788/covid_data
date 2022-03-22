import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
record = SHEET.worksheet('record')

data = record.get_all_values()
"""

def get_record_data()

"""
Record covid data from the user
"""

    while True:
        print("Please record covid cases from todays date")
        print("The following headings must be updated\n")
        print("Date, CovidConfirmed, Hopitalised, Male, Female, TotalDeaths")
        print("Example: DDMMYYYY,1,0,0,1,0\n")

        data_str = input("Enter your data here:")

        record_data = data_str.split(",")
        
        if validate_data(record_data):
            print("Data is valid")
            break

    return record_data

def validate_data(values):
    """
    all values to integers
    presents error if cannot convert string to integers
    looks for exactly 6 inputs with the first input a date
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def update_record_worksheet(data):
    """
    updating the worksheet from the user inputs 
    """
    print("updating record worksheet\n")
    record_worksheet = SHEET.worksheet("record")
    record_worksheet.append_row(data)
    print("Data Recorded Succesfully")

def calculate_covid_data(summary):
    """
    Get totals after data entry

    """
    print("Updating covid data total results show...\n")
    summary = SHEET.worksheet("summary").get_all_values()
    summary_row = summary[-1]
    print(summary_row)

def main():
    """
    Run all functions 
    """
    data = get_record_data()
    record_data= [int(num) for num in data]
    update_record_worksheet(record_data)
    calculate_covid_data(record_data)


print("Welcome to Covid Data Entry and Stats\n")
main()