#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less = "Last digit of {:d} is {:d} and is less than 6 and not 0"
greater = "Last digit of {:d} is {:d} and is greater than 5"
zero = "Last digit of {:d} is 0 and is 0"
if number < 0:
    positive = number * -1
    last_digit = positive % 10
    last_digit = last_digit * -1
if number > 0:
    last_digit = number % 10

if last_digit < 6 & last_digit != 0:
    print(less.format(number, last_digit))
elif last_digit > 5:
    print(greater.format(number, last_digit))
elif last_digit == 0:
    print(zero.format(number))
