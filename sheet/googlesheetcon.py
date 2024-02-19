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

# selection function to help test the various functionalities of the code
def selection():
    selected_number = int(input(
        """
        Make a selection on the various options below based on what you want to do on our platform.

        Options:
        1. View Data
        2. Add Data
        3. Delete

        """
    ))
    return selected_number


# data input function
def input_data():
    name = str(input("Name: "))
    age = int(input("Age: "))
    image_link = str(input("Image: "))
    return name, age, image_link

# Main code functions
# function for adding data into the spreadsheet
def add_data(name, age, inage_link):
    update_data = [name, age, image_link]

    # appending to the file
    worksheet.append_row(update_data)


# function for fetching data from spreadsheet
def fetch_data():
# Print all data in files
    print("items                   " + "                  descriptions                   " + "          image" )
    for rows in sheet[1:]:
        print(rows[0], "                    ", rows[1], "                      ", rows[2])


# function for deleting a particular dataset from the spreadsheet
def delete_data():
    # this will print out the list with numbers, then the user make selection of the number which comes as the array
    print("working on the delete function")



# calling for the functions above
num = selection()
if num == 2:
    name, age = input_data()
    add_data(name, age)

elif num == 1:
    fetch_data()

elif num ==  3:
    delete_data()





