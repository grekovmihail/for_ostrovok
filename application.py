import datetime
import urllib.parse
from urllib.request import urlopen

from bs4 import BeautifulSoup

from utils.input_format import input_format
from utils.input_month import input_month
from utils.input_year import input_year

if __name__ == '__main__':

    month, month_name = input_month()
    now = datetime.datetime.now()
    year = input_year(now)

    if (year == now.year) & \
            (month + 1 > now.month):
        print("Простите, но это будующее")
        input_month()
        input_year(now)

    if (month > 1) & (month < 10):
        month = "0" + str(month)

    format = input_format()
    try:
        url = urlopen("https://www.smashingmagazine.com/" + str(year) + "/" + str(
            month) + "/desktop-wallpaper-calendars-" + month_name + "-" + str(year)).read() #Можно было бы сделать рекурсивный поиск ссылок, но в любом случай надо было дописывать год и месяц и большие затраты времени
        soup = BeautifulSoup(url, "html.parser")

        for line in soup.find_all('a'):
            name = str(line.get('href'))
            if format in name:
                print(name)
                url = name
                img = urllib.request.urlopen(url).read()
                name = name.split('/')
                out = open(name[len(name) - 1], "wb")
                out.write(img)
                out.close
    except:
        print("something is wrong")
