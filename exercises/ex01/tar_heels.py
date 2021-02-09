"""An exercise in remainders and boolean logic."""

__author__ = "730322345"


# Begin your solution here...
integer = int(input("Enter a number: "))
th = "CAROLINA"
if integer % 7 == 0:
    th = "TAR"
if integer % 2 == 0:
    if th == "CAROLINA":
        th = "HEELS"
    else:
        th += " HEELS"
print (th)