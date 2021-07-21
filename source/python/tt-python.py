import datetime
import humanize


if __name__ == '__main__':
    hrs_left = int(input("Enter the # of hours remaining on trader:"))
    date_end = (datetime.datetime.now() + datetime.timedelta(hours=(hrs_left))).strptime("%a %b %I:%M %p, %d %B %Y") "ddd MMM Do YYYY at h:m a");
    print(date_end)
