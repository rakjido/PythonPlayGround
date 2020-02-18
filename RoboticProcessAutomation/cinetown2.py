# cinetown2.py

import datetime
import urllib.request

from rpa_utils import getdigit

weeks = ['월','화','수','목','금','토','일']

missing_all = open('missing_all.txt', 'r')

# while True:
#     line = missing_all.readline()
#     if not line: break
#     print(line.strip('\n'))


lines = missing_all.readlines()
for line in lines:
    file_name = line.strip('\n')
    year = int(file_name[:4])
    month = int(file_name[4:6])
    day = int(file_name[6:8])
    base_date = datetime.date(year, month, day)
    week = base_date.weekday()
    try:
        # from 2016.10.19 to present
        if base_date >= datetime.date(2016,10,19):
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-v2000008804-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date >= datetime.date(2016,10,13) and base_date <= datetime.date(2016,10,18):
        # from 2016.10.13 to 2016.10.18 
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-pc-v2000008804-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date >= datetime.date(2016,10,1) and base_date <= datetime.date(2016,10,12):
        # from 2016.10.01 to 2016.10.12
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-pc-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date <= datetime.date(2016,9,30):
        # from to 2016.09.30
            urls = "http://podcastfile.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-pc-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"

        files = "cinetown" + str(year) + getdigit(month) + getdigit(day) + "(" + weeks[week] + ").mp3"
        urllib.request.urlretrieve(urls,files)
    except urllib.error.HTTPError as e:
        file_play = open('missing_after_all.txt', 'a')
        file_play.write(files+"\n")
        file_play.close()
        # print(urls)
        print(files)

missing_all.close()

