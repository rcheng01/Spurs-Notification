import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime
import sms

while True:

    # Get current time and date
    now = datetime.now()
s
    current_month = now.strftime("%B")
    current_day = now.strftime("%d")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")

    # Make Beautiful Soup of website
    url = "https://www.skysports.com/tottenham-hotspur-fixtures"
    website = requests.get(url)
    soup = BeautifulSoup(website.text, "lxml")

    # Get match date
    dates = str(soup.find(class_="fixres__header2"))
    match_date = dates[28:-5]
    match_date = match_date.split()

    match_month = match_date[2]
    match_day_info = [s for s in match_date[1] if s.isdigit()]

    match_day = ""
    for i in match_day_info:
        match_day += i

    # Get match time
    match_time = str(soup.find(class_="matches__date"))
    match_hour_unadjusted = match_time[37:39]
    match_minute = match_time[40:-11]
    match_hour = str(int(match_hour_unadjusted) - 5)  # adjust for time zone difference

    # Get other team's name
    other_team = str(soup.findAll(class_="swap-text__target")[1])
    other_team = other_team[32:-7]

    # Send notification if five minutes from match
    if (match_month == current_month) and (match_day == current_day) and (match_hour == current_hour):
        if int(current_minute) + 5 == int(match_minute):
            sms.send_notification(other_team)
            time.sleep(350)








