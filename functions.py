import datetime
import os
import shutil
import User_input

# list of file extensions for photos of videos
list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']


# removes all folders
def folder_remover():
    for path, dirs, files in os.walk(User_input.file_path, topdown=False):
        if path != User_input.file_path:
            for filename in files:
                os.rename(os.path.join(path, filename), os.path.join(User_input.file_path, filename))
            if str(path) != str(User_input.file_path):
                os.rmdir(path)


# function that sorts files into years
def year_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = min(os.path.getmtime(file), os.path.getctime(file))
            readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
            readable_date = readable_date.replace("-", " ")
            year, month, day, time = readable_date.split(" ")

            year_path = User_input.file_path.joinpath(year)
            if not year_path.exists():
                year_path.mkdir()

            shutil.move(str(file), str(year_path) + "/" + file.name)


# function that sorts files into years, then months
def month_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = min(os.path.getmtime(file), os.path.getctime(file))
            readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
            readable_date = readable_date.replace("-", " ")
            year, month, day, time = readable_date.split(" ")
            month_name = list_of_months[int(month) - 1]

            year_path = User_input.file_path.joinpath(year)
            if not year_path.exists():
                year_path.mkdir()

            month_path = year_path.joinpath(month_name)
            if not month_path.exists():
                month_path.mkdir()

            shutil.move(str(file), str(year_path) + "/" + str(month_name) + "/" + file.name)


# function that sorts files into year, then month, then day of month
def day_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = min(os.path.getmtime(file), os.path.getctime(file))
            readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
            readable_date = readable_date.replace("-", " ")
            year, month, day, time = readable_date.split(" ")
            month_name = list_of_months[int(month) - 1]

            year_path = User_input.file_path.joinpath(year)
            if not year_path.exists():
                year_path.mkdir()

            month_path = year_path.joinpath(month_name)
            if not month_path.exists():
                month_path.mkdir()

            day_path = month_path.joinpath(day)
            if not day_path.exists():
                day_path.mkdir()

            shutil.move(str(file), str(year_path) + "/" + str(month_name) + "/" + str(day) + "/" + file.name)


# function that sorts files into two into a folder that has the name of the month and the year
def my_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = min(os.path.getmtime(file), os.path.getctime(file))
            readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
            readable_date = readable_date.replace("-", " ")
            year, month, day, time = readable_date.split(" ")
            month_name = list_of_months[int(month) - 1]

            my_path = User_input.file_path.joinpath(f'{month_name} {year}')
            if not my_path.exists():
                my_path.mkdir()

            shutil.move(str(file), str(my_path) + "/" + file.name)
