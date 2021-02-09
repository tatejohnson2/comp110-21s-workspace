"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta
from math import ceil, floor


# Begin your solution here...
population = int(input("Population: "))
administered = int(input("Doses administered: "))
doses_per_day = int(input("Doses per day: "))
target = int(input("Target percent vaccinated: "))

target_pop_num = population * target / 100.0
pop_left_to_target = target_pop_num - (administered / 2.0)
days_left = floor(2.0 * pop_left_to_target / doses_per_day)
#msg = "We will reach 80% vaccination in 364 days, which falls on February 02, 2022."
today = datetime.today()
days = timedelta(days_left)
date = today + days
msg = "We will reach " + str(target) + "% vaccination in " + str(days_left) + " days, which falls on " + date.strftime("%B %d, %Y")
print (msg)