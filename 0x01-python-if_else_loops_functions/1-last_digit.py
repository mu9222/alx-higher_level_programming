#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit < 6 and last_digit != 0:
    print("Last digit of {number: d} is {last_digit: d} and not 0")
if last_digit > 5:
    print("Last digit of {number: d} is {last_digit: d} and greater than 5")
if last_digit == 0:
    print("Last digit of {number: d} is 0 and is 0)
