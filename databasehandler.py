import win32api
import sqlite3
import os
import json

conn = sqlite3.connect('movies.db')

cwd = os.getcwd()
data = {}

with open(os.path.join(cwd,'temp_data.json'),'r+') as fp:
    data = json.load(fp)

c = conn.cursor()

c.execute("""CREATE TABLE local_movies(
        serial integer,
        file_name text,
        name text,
        rating real,
        release_date text,
        director text,
        language text,
        synopsis text,
        poster text
        )""")

# drives = []
# for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
#     drives.append(drive)
# systemdrive = os.environ['SYSTEMDRIVE']
# filenames = []

# for drive in drives:
#     if(systemdrive not in drive):
#         top = drive
#         for dirName, subdirList, fileList in os.walk(drive):
#             try:
#                 for filename in fileList:
#                     os.chdir(dirName)
#                     if ((filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi") or filename.endswith(".m4v") or filename.endswith(".flv")) and os.stat(os.path.join(os.getcwd(),filename)).st_size > 500000000):
#                         if(filename not in filenames):
#                             filenames.append(filename)
#                             print(filename)
#                             os.chdir(top)
#             except(FileNotFoundError):
#                 continue

# films_in_db = {}
# films_in_db["names"] = filenames

# films_not_in_database = []

# for movies in films_in_db:
#     if movies not in data:
#         films_not_in_database.append(movies)



conn.commit()
conn.close()