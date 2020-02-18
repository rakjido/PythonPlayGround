# -*- coding: utf-8 -*-

from os import listdir
from os.path import splitext, isfile
import datetime

from rpa_utils import getdigit

weeks = ['월','화','수','목','금','토','일']

original_dir = '/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation'

# file list in the folder
file_list = listdir(original_dir)


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

        if isfile(original_dir + "/" + files)==False:
            # 2019.07.14부터 일요일도 방송
            if week==6:
                if base_date >= datetime.date(2019,7,14):
                    print(files)
            else:
                print(files)
        # print(files)
        # print("cinetown20200131(금).mp3" in file_list)
        # print("cinetown20200131(금).mp3" in file_list)
        # # if (files in file_list) == True:
        #     print("Yes", files)
        # else:
        #     print("No", files)
    except Exception as e:
        print(e)

    base_date = base_date - datetime.timedelta(days=1)
    

        # with open('missing_file_check.txt', 'a') as f:
        #     f.write(files+"\n")
        #     f.close()
        #     # print(urls)
        #     print(files)



# print(file_list)


# for f_name in file_list:    
#     if splitext(f_name)[1] == ".mp3":
#         print(f_name)
