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


record = SHEET.worksheet('record')
summary = SHEET.worksheet('summary')

record_data = record.get_all_values()
summary_data = summary.get_all_values()


def get_record_data():
    """
    Record covid data from the user

    """

    while True:
        print("Please record covid cases from todays date")
        print("The following headings must be updated\n")
        print("CovidConfirmed, Hopitalised, Male, Female, TotalDeaths")
        print("Example: 1,0,0,1,0\n")

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
        if len(values) != 5:
            raise ValueError(
                f"5 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"❌  : {e}, please try again.\n")
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

def calculate_covid_data(summary_data):
    """
    Get totals after data entry

    """

    print("Updating covid data total results show...\n")
    record = SHEET.worksheet("record").get_all_values()
    record_row = record[-1]
    """print(f"summary row: {summary_row}")"""
    summary_data = []
    for summary, record in zip(summary_row, record_row):
        summary = int(summary) + record
        summary_data.append(summary)

    print(summary_data)

def update_summary_worksheet(data):
    """
    Updates the work sheet to include the new data just entered

    """
    print("updating summary worksheet\n")
    summary_worksheet = SHEET.worksheet("summary")
    summary_worksheet.append_row(data)

    print("Data Recorded Succesfully")

def main():
    """
    Run all functions 
    """
    data = get_record_data()
    record_data= [int(num) for num in data]
    summary_data=[int(num)for num in data]
    update_record_worksheet(record_data)
    calculate_covid_data(summary_data)
    new_summary_data = calculate_covid_data(summary_data)
    print(new_summary_data)


print("Welcome to Covid Data Entry and Stats\n")
main()