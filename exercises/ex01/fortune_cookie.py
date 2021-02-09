"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730322345"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

num = randint(1,4)
if num == 1:
    print('Help me, I\'m stuck in a fortune cookie factory')
else:
    if num == 2:
        print ('Your life will go according to plan')
    else:
        if num == 3:
            print('Be helpful to your friends')
        else:
            if num == 4:
                print ('Wear socks with your flip flops tomorrow')

print("Now, go spread positive vibes!")
