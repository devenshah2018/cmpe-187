# TODO
# Function that validates the format of the input date and raises an error if the input is not in the correct format
def checkFormat(date):
    import datetime
    datetime.datetime.strptime(date, '%m/%d/%Y')


# Function that checks if a year is a leap year
def isLeapYear(year):
    leap = False
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
    elif (year % 4 == 0) and (year % 100 != 0):
        leap = True
    else:
        leap = False
    return leap


# Function that prints out the next date
def nextDate(date):
    print("Input date: " + date)

    # Checks format of date
    checkFormat(date)

    # Initialize variables
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])

    # Check input range
    if year < 1900 or year > 2099:
        print("Year is out of range. Please enter a year that is inclusive between 1900 and 2099.")
        return

    # Advances the day by one
    day += 1

    # Arrays of months that have 31 and 30 days, respectively
    months_31_days = [1, 3, 5, 7, 8, 10]
    months_30_days = [4, 6, 9, 11]

    # Checks if it's the last day of a month that has 31 days
    if (day == 32 and month in months_31_days):
        month += 1
        day = 1

    # Checks if it's the last day of a month that has 30 days
    if (day == 31 and month in months_30_days):
        month += 1
        day = 1

    # Checks if it's the last day of February
    if (month == 2 and day == 30 and isLeapYear(year)):  # Leap year
        month += 1
        day = 1
    elif (month == 2 and day == 29 and not isLeapYear(year)):  # Not a leap year
        month += 1
        day = 1

    # Check if date is the last date of the year
    if (month == 12 and day == 32):
        month = 1
        day = 1
        year += 1

    # Formatting and printing out the date only if the year is between 1900 and 2099 inclusively
    if (len(str(month)) < 2 and len(str(day)) < 2):  # Add 0 before the month and day
        print("Next date: 0" + str(month) +
              "/0" + str(day) + "/" + str(year))
    elif (len(str(month)) < 2):  # Add 0 before the month
        print("Next date: 0" + str(month) +
              "/" + str(day) + "/" + str(year))
    elif (len(str(day)) < 2):  # Add 0 before the day
        print("Next date: " + str(month) +
              "/0" + str(day) + "/" + str(year))
    else:
        print("Next date: " + str(month) +
              "/" + str(day) + "/" + str(year))


def main():
    date = input("Enter date (MM/DD/YYYY): ")

    # Prints out the next date and raises a ValueError if the date is not in the correct format
    try:
        nextDate(date)
    except ValueError:
        print('Invalid format. Please enter a valid date using the format (MM/DD/YYYY).')


if __name__ == "__main__":
    main()
