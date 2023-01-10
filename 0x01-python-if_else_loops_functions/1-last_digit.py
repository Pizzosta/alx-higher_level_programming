#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
ld = (number[-1:])
ld = int(ld)
if (ld > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, ld))
if (ld == 0):
    print("Last digit of {} is {} and is 0".format(number, ld))
if ((ld < 6) & (ld != 0)):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, ld))
