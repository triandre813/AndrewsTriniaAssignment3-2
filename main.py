# Function:  This program determines if a date entered by the user is valid.
# Input:     Interactive
# Output:    Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAYS_IN_MONTH = {
    1: 31,  # January
    2: 29,  # February (considering leap years, 29 is the maximum)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

year = None
month = None
day = None

# Get the year, then the month, then the day
# housekeeping()
year = input("Enter the year: ")
month = input("Enter the month: ")
day = input("Enter the day: ")

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAYS_IN_MONTH[int(month)]: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

if validDate:
    print(month + "/" + day + "/" + year + " is a valid date. ") # Output statement
else:
    print(month + "/" + day + "/" + year + " is an invalid date. ") # Output statement
  
