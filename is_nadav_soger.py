import datetime
import calendar
from datetime import date
def nadav():
    calendar.setfirstweekday(calendar.SUNDAY)
    month = int(input("Enter Month: "))
    day = int(input("Enter Day: "))

    my_date = datetime.date(2022, month, day)
    year, week_num, day_of_week = my_date.isocalendar()

    if month > 12:
        print("The month you entered is not invaild")
        month = int(input("Enter Month: "))
    if day_of_week == 7:
        week_num -= 1
    if week_num % 2 == 0:
        print("Nadav is going HOME!")
    else:
        print("Nadav Soger!")
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        nadav()
    if restart == "n" or restart == "no":
        print("Bye...")


nadav()