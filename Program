import datetime
import os
from pathlib import Path
import shutil

#prompts user to enter the path to the folder
print("Please insert the path to the folder you would like sorted:")
file_path = Path(input())

#incase the user enters a invalid path
while file_path.is_file() or file_path.is_dir() == False:
    print(f"invalid path\nPlease try again:")
    file_path = Path(input())

#creates path to the folders if they do not already exist
photos_path = file_path.joinpath("Photos")
videos_path = file_path.joinpath("Videos")
if not photos_path.exists():
    photos_path.mkdir()
if not videos_path.exists():
    videos_path.mkdir()

#list of file extentions for photos of videos
photo_ext = [".jpg", ".png", ".webp", ".svg", ".jpeg", ".jfif", ".pjpeg", ".pjp",
             ".gif", ".apng", ".avif", ".tif", ".tiff", ".ico", ".cur", ".bmp", ".jpe",
             ".jif", ".jfi", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".dib",
             ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf",
             '.jpx', ".jpm", ".mj2", ".svgz", ".ai", ".eps", ".pdf"]

video_ext = [".webm", ".mkv", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gifv", ".mng",
             ".avi", ".mts", ".m2ts", ".ts", ".mov", ".qt", ".wmv", ".yuv", ".rmvb",
             ".rm", ".viv", ".asf", ".amv", ".mp4", ".m4p", ".m4v", ".mpg", ".mpeg",
             ".mpv", ".mpe", ".mp2", ".m2v", ".svi", ".3gp", ".3g2", ".mxf", ".roq",
             ".nsv", ".flv", ".f4v", ".f4v", ".f4p", ".f4a", ".f4b"]

#iterates through each file in the selected folder
for file in file_path.iterdir():

    #Checks to see if its a valid file and not just a folder
    if file.is_file():

        #grabs the creation date of the file and cleans up the format so its human readable
        non_readable_date = os.path.getctime(file)
        readable_date = str(datetime.datetime.fromtimestamp(non_readable_date))
        readable_date = readable_date.replace("-", " ")
        year, month, day, time = readable_date.split(" ")

        #grabs file extenstion
        file_ext = file.suffix

        #Checks if the file is a photo
        if file_ext.lower() in photo_ext:
            # checks to see if the folder for the year has been created
            year_path = photos_path.joinpath(year)
            if not year_path.exists():
                year_path.mkdir()
            shutil.move(str(file), str(photos_path) + "/" + year + "/" + file.name)

        #Checks if the file is a video
        elif file_ext.lower() in video_ext:
            # checks to see if the folder for the year has been created
            year_path = videos_path.joinpath(year)
            if not year_path.exists():
                year_path.mkdir()
            shutil.move(str(file), str(videos_path) + "/" + year + "/" + file.name)

        #if the file is neither a video nor a photo
        else:
            other_path = file_path.joinpath("Other")
            if not other_path.exists():
                other_path.mkdir()
            shutil.move(str(file), str(other_path) + "/" + file.name)
