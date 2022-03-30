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


record = SHEET.worksheet('record')
summary = SHEET.worksheet('summary')

record_data = record.get_all_values()
summary_data = summary.get_all_values()

"""
Adapted from Love Sandwiches
"""


def get_record_data():
    """
    Record covid data from the user

    """

    while True:
        print("Please record covid cases from today")
        print("The following headings must be updated\n")
        print("CovidConfirmed, Hopitalised, Male, Female, TotalDeaths")
        print("Example: 1,0,0,1,0\n")

        data_str = input("Enter your data here:\n")

        record_data = data_str.split(",")
        if validate_data(record_data):
            print("Data is valid")
            break

    return record_data


def validate_data(values):
    """
    All values to integers
    Presents error if cannot convert string to integers
    Looks for exactly 5 inputs with the first input a date
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


def calculate_covid_data(summary_data):
    """
    Updates totals after data entry

    """

    print("Updating covid data total results show...\n")
    record = SHEET.worksheet("record").get_all_values()
    print(f"RECORD SHEET: {record}")
    record_row = record[-1]
    print(f"RECORD ROW: {record_row}")
    summary = SHEET.worksheet("summary").get_all_values()
    print(f"SUMMARY SHEET: {summary}")
    summary_row = summary[-1]
    print(f"SUMMARY ROW: {summary_row}")

    new_summary_data = []

    for x in range(len(record_row)):
        new_summary_data.append(int(summary_row[x]) + int(record_row[x]))
    print(f"NEW SUMMARY: {new_summary_data}")

    return new_summary_data


def update_worksheet(data, worksheet):
    """
    updates the worksheets accordingly for both record and summary
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def get_last_entry_summary():
    """
    provides totals of the summary sheet with covid
     """
    summary = SHEET.worksheet("summary")
    columns = []

    for ind in range(1, 6):
        column = summary.col_values(ind)
        columns.append(column[-1:])
    print(f"{columns}\n Summary Totals were successfully updated\n")


def get_total_hospitalised_covid():
    """
    provides totals of the summary sheet with covid
     """
    summary = SHEET.worksheet("summary")

    columns = []
    column = summary.col_values(2)
    columns.append(column[-1])
    print(f"{columns} Total Hospitalised with Covid\n")


def get_total_males_covid():
    """
    provides total males with covid

     """
    summary = SHEET.worksheet("summary")

    columns = []
    column = summary.col_values(3)
    columns.append(column[-1])
    print(f"{columns} Total males with Covid\n")


def get_total_females_covid():
    """
    provides total females with covid
     """
    summary = SHEET.worksheet("summary")

    columns = []
    column = summary.col_values(4)
    columns.append(column[-1])
    print(f"{columns} Total Females with Covid\n")


def get_total_deaths_covid():
    """
    provides total deaths with covid
     """
    summary = SHEET.worksheet("summary")

    columns = []
    column = summary.col_values(5)
    columns.append(column[-1])
    print(f"{columns} Total Covid Deaths\n")


def main():
    """
    Run all functions
    """
    data = get_record_data()
    record_data = [int(num) for num in data]
    summary_data = [int(num)for num in data]
    update_worksheet(record_data, "record")
    calculate_covid_data(record_data)
    new_summary_data = calculate_covid_data(summary_data)
    update_worksheet(new_summary_data, "summary")
    get_last_entry_summary()
    get_total_hospitalised_covid()
    get_total_males_covid()
    get_total_females_covid()
    get_total_deaths_covid()


print("Welcome to Covid Data Entry and Stats\n")
main()
