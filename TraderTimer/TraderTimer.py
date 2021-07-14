import datetime


if __name__ == '__main__':
    hrs_left = int(input("Enter the # of hours remaining on trader:"))
    date_end = (datetime.datetime.now() + datetime.timedelta(hours=(hrs_left))).strftime("%I:%M %p, %d %B %Y")
    print(date_end)
