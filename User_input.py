from pathlib import Path
import Input_functions

#   ++++++++++++++++++++ USER INPUT ++++++++++++++++++++++++++++++

# prompts user to enter the path to the folder

print("Please insert the path to the folder you would like sorted:")
file_path = Path(input().replace("\"", ""))


# incase the user enters an invalid path
while file_path.is_file() or file_path.is_dir() is False:
    print(f"invalid path\nPlease try again:")
    file_path = Path(input().replace("\"", ""))


# Asks user if they would like to sort the files by year
year_yn = Input_functions.year_input()

month_yn  = False
day_yn    = False
pv_folder = False
m_y_input = False

# If user said yes, it then asks them if they want to sort files by months
if year_yn:
    month_yn = Input_functions.month_input()

    # If user said yes, it then asks them if they want to sort files by days
    if month_yn:
        day_yn = Input_functions.day_input()

# If user does not want to sort by year, the program asks if they want to sort by month and year
else:
    m_y_input = Input_functions.month_year_input()

# Asks user if they want there files separated into two category, photos and videos
pv_folder = Input_functions.pv_input()

# List of what the user has inputed
qa_input = (year_yn, month_yn, day_yn, pv_folder, m_y_input)

print(qa_input)