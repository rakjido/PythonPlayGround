# cinetown.py

import datetime
import urllib.request

from rpa_utils import getdigit

weeks = ['월','화','수','목','금','토','일']

fr_date = datetime.date(2020,2,2)
to_date = datetime.date(2015,11,2)
base_date = fr_date
while base_date >= to_date:
    year = base_date.year
    month = base_date.month
    day = base_date.day
    week = base_date.weekday()

    try:
        if base_date >= datetime.date(2017,8,5):
            # from 2017.08.05 to present
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-v2000008804-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date >= datetime.date(2017,6,9):
            # from 2017.06.09 to  2017.08.04
            urls = "http://podcastfile.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-v0000376638-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date >= datetime.date(2016,10,19):
            # from 2016.10.19 to 2017.06.08
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-v2000008804-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date >= datetime.date(2016,10,13):
            # from 2016.10.13 to 2016.10.18 
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-pc-v2000008804-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        elif base_date >= datetime.date(2016,10,1):
            # from 2016.10.01 to 2016.10.12 
            urls = "http://podcastfile2.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-pc-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"
        else:
            # from to 2016.09.30
            urls = "http://podcastfile.sbs.co.kr/powerfm/" + str(year) + "/" + getdigit(month) + "/power-pc-" + str(year)+getdigit(month)+getdigit(day) + "(11-00).mp3"

        files = "cinetown" + str(year) + getdigit(month) + getdigit(day) + "(" + weeks[week] + ").mp3"
        urllib.request.urlretrieve(urls,files)
    except urllib.error.HTTPError as e:
        file_play = open('missing_files.txt', 'a')
        file_play.write(files+"\n")
        file_play.close()
        # print(urls)
        print(files)

    base_date = base_date - datetime.timedelta(days=1)
    

