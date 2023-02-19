#12.    Write a program to display day of the week., Mon, Tue, Wed, Thu, Fri, Sat, Sun

import calendar
def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))   
    dayNumber = calendar.weekday(year, month, day)
    days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
    return (days[dayNumber])
date = '23 10 2024'
print(findDay(date))
