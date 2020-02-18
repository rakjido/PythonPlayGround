# -*- coding: utf-8 -*-

from os import listdir, remove
from os.path import splitext, isfile, dirname, abspath, join
import datetime

from rpa_utils import getdigit

weeks = ['월','화','수','목','금','토','일']

#original_dir = '/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation'
original_dir = dirname(abspath(__file__))




fr_date = datetime.date(2020,2,2)
to_date = datetime.date(2015,11,2)
base_date = fr_date
while base_date >= to_date:
    year = base_date.year
    month = base_date.month
    day = base_date.day
    week = base_date.weekday()

    try:
        files =   "cinetown" + str(year) + getdigit(month) + getdigit(day) + "(" + weeks[week] + ").mp3"
        
        # 2019.07.14부터 일요일도 방송
        if week==6:
            if base_date < datetime.date(2019,7,14):
                #remove(join(original_dir,files))
                print(original_dir + "/" + files)
                remove(original_dir + "/" + files)
    except Exception as e:
        print(e)

    base_date = base_date - datetime.timedelta(days=1)

# file list in the folder
# file_list = listdir(original_dir)

# for file in file_list:
#     if splitext(file)[1] == '.mp3':
#         year = int(file[8:12])
#         month = int(file[12:14])
#         day = int(file[14:16])
#         base_date = datetime.date(year, month, day)
#         week = base_date.weekday()
       
#         if base_date < datetime.date(2019,7,14) and week==6:
#             print(base_date, file, week)
