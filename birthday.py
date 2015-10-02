"""
birthday.py
Author: Sawyer Hanlon
Credit: Jeff
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

month2 = month_name[todaymonth]

name = input("Hello, what is your name? ")
month = input("Hi "+name+", what was the name of the month you were born in? ")
year = int(input("And what year were you born in, "+name+"? "))
day = int(input("And the day? "))

#B-Day
if month==month2 and day==todaydate:
    print("Happy birthday!")

#Halloween
elif day==31 and month=="October":
    print("Your were born on Halloween!")

#Winter months
else:
    if year<=1979 and month == "December":
        print("{0}, you are a winter baby of the stone age.".format(name))
    if year<=1979 and month == "January":
        print("{0}, you are a winter baby of the stone age.".format(name))
    if year<=1979 and month == "February":
        print("{0}, you are a winter baby of the stone age.".format(name))
    
    if year>=1980 and year<=1989 and month == "December":
        print("{0}, you are a winter baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "January":
        print("{0}, you are a winter baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "February":
        print("{0}, you are a winter baby of the eighties.".format(name))
        
    if year>=1990 and year<=1999 and month == "December":
        print("{0}, you are a winter baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "January":
        print("{0}, you are a winter baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "February":
        print("{0}, you are a winter baby of the nineties.".format(name))
        
    if year>=2000 and month == "December":
        print("{0}, you are a winter baby of the two thousands.".format(name))
    if year>=2000 and month == "January":
        print("{0}, you are a winter baby of the two thousands.".format(name))
    if year>=2000 and month == "February":
        print("{0}, you are a winter baby of the two thousands.".format(name))
    
    #Spring months
    if year<=1979 and month == "March":
        print("{0}, you are a spring baby of the stone age.".format(name))
    if year<=1979 and month == "April":
        print("{0}, you are a spring baby of the stone age.".format(name))
    if year<=1979 and month == "May":
        print("{0}, you are a spring baby of the stone age.".format(name))
    
    if year>=1980 and year<=1989 and month == "March":
        print("{0}, you are a spring baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "April":
        print("{0}, you are a spring baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "May":
        print("{0}, you are a spring baby of the eighties.".format(name))
    
    if year>=1990 and year<=1999 and month == "March":
        print("{0}, you are a spring baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "April":
        print("{0}, you are a spring baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "May":
        print("{0}, you are a spring baby of the nineties.".format(name))
    
    if year>=2000 and month == "March":
        print("{0}, you are a spring baby of the two thousands.".format(name))
    if year>=2000 and month == "April":
        print("{0}, you are a spring baby of the two thousands.".format(name))
    if year>=2000 and month == "May":
        print("{0}, you are a spring baby of the two thousands.".format(name))
        
    #Summer Months
    if year<=1979 and month == "June":
        print("{0}, you are a summer baby of the stone age.".format(name))
    if year<=1979 and month == "July":
        print("{0}, you are a summer baby of the stone age.".format(name))
    if year<=1979 and month == "August":
        print("{0}, you are a summer baby of the stone age.".format(name))
    
    if year>=1980 and year<=1989 and month == "June":
        print("{0}, you are a summer baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "July":
        print("{0}, you are a summer baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "August":
        print("{0}, you are a summer baby of the eighties.".format(name))
    
    if year>=1990 and year<=1999 and month == "June":
        print("{0}, you are a summer baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "July":
        print("{0}, you are a summer baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "August":
        print("{0}, you are a summer baby of the nineties.".format(name))
    
    if year>=2000 and month == "June":
        print("{0}, you are a summer baby of the two thousands.".format(name))
    if year>=2000 and month == "July":
        print("{0}, you are a summer baby of the two thousands.".format(name))
    if year>=2000 and month == "August":
        print("{0}, you are a summer baby of the two thousands.".format(name))
        
    #Fall Months
    if year<=1979 and month == "September":
        print("{0}, you are a fall baby of the stone age.".format(name))
    if year<=1979 and month == "October":
        print("{0}, you are a fall baby of the stone age.".format(name))
    if year<=1979 and month == "November":
        print("{0}, you are a winter baby of the stone age.".format(name))
    
    if year>=1980 and year<=1989 and month == "September":
        print("{0}, you are a fall baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and day and month == "October":
        print("{0}, you are a fall baby of the eighties.".format(name))
    if year>=1980 and year<=1989 and month == "November":
        print("{0}, you are a winter baby of the eighties.".format(name))
        
    if year>=1990 and year<=1999 and month == "September":
        print("{0}, you are a fall baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "October":
        print("{0}, you are a fall baby of the nineties.".format(name))
    if year>=1990 and year<=1999 and month == "November":
        print("{0}, you are a fall baby of the nineties.".format(name))
        
    if year>=2000 and month == "September":
        print("{0}, you are a fall baby of the two thousands.".format(name))
    if year>=2000 and month == "October":
        print("{0}, you are a fall baby of the two thousands.".format(name))
    if year>=2000 and month == "November":
        print("{0}, you are a fall baby of the two thousands.".format(name))


    





