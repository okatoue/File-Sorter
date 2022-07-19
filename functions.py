import datetime
import os
from pathlib import Path
import shutil
import User_input

# list of file extensions for photos of videos


photo_ext = [".jpg", ".png", ".webp", ".svg", ".jpeg", ".jfif", ".pjpeg", ".pjp",
             ".gif", ".apng", ".avif", ".tif", ".tiff", ".ico", ".cur", ".bmp", ".jpe",
             ".jif", ".jfi", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".dib",
             ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf",
             '.jpx', ".jpm", ".mj2", ".svgz", ".ai", ".eps", ".pdf"]

video_ext = [".webm", ".mkv", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gifv", ".mng",
             ".avi", ".mts", ".m2ts", ".ts", ".mov", ".qt", ".wmv", ".yuv", ".rmvb",
             ".rm", ".viv", ".asf", ".amv", ".mp4", ".m4p", ".m4v", ".mpg", ".mpeg",
             ".mpv", ".mpe", ".mp2", ".m2v", ".svi", ".3gp", ".3g2", ".mxf", ".roq",
             ".nsv", ".flv", ".f4v", ".f4v", ".f4p", ".f4a", ".f4b", ".wav"]

list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']


def year_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = os.path.getmtime(file)
            readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
            readable_date = readable_date.replace("-", " ")
            year, month, day, time = readable_date.split(" ")

            year_path = User_input.file_path.joinpath(year)
            if not year_path.exists():
                year_path.mkdir()

            shutil.move(str(file), str(year_path) + "/" + file.name)


def month_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = os.path.getmtime(file)
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


def day_only():
    for file in User_input.file_path.iterdir():

        if file.is_file():
            non_readable_date = os.path.getmtime(file)
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


def year_pv():
    print("not done")


def month_pv():
    print("not done")


def day_pv():
    print("not done")


def my_only():
    print("not done")


def my_pv():
    print("not done")



#
# # iterates through each file in the selected folder
# for file in User_input.file_path.iterdir():
#
#     # Checks to see if it's a valid file and not just a folder
#     if file.is_file():
#
#         # grabs the creation date of the file and cleans up the format so its human-readable
#         non_readable_date = os.path.getmtime(file)
#         readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
#         readable_date = readable_date.replace("-", " ")
#         year, month, day, time = readable_date.split(" ")
#
#         # checks to see if the year already has a dedicated folder
#         year_path = User_input.file_path.joinpath(year)
#         if not year_path.exists():
#             year_path.mkdir()
#
#         # grabs file extension
#         file_ext = file.suffix
#
#         # Checks if the file is a photo
#         if file_ext.lower() in PHOTO_EXT:
#             shutil.move(str(file), year + "/" + photos_path + "/" + file.name)
#
#         # Checks if the file is a video
#         elif file_ext.lower() in VIDEO_EXT:
#             # checks to see if the folder for the year has been created
#             year_path = videos_path.joinpath(year)
#             if not year_path.exists():
#                 year_path.mkdir()
#             shutil.move(str(file), str(videos_path) + "/" + year + "/" + file.name)
#
#         # if the file is neither a video nor a photo
#         else:
#             other_path = User_input.file_path.joinpath("Other")
#             if not other_path.exists():
#                 other_path.mkdir()
#             shutil.move(str(file), str(other_path) + "/" + file.name)
#
#         # creates path to the folders if they do not already exist
#         photos_path = User_input.file_path.joinpath("Photos")
#         videos_path = User_input.file_path.joinpath("Videos")
#         if not photos_path.exists():
#             photos_path.mkdir()
#         if not videos_path.exists():
#             videos_path.mkdir()
