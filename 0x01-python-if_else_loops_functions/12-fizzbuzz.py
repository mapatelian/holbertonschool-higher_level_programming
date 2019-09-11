#!/usr/bin/bash
def fizzbuzz():
    for i in range(0, 101):
        if i % 3 and i % 5:
            print("FizzBuzz ", end='')
        if i % 3:
            print("Fizz ", end='')
        if i % 5:
            print("Buzz ", end='')
        else:
            print(i + ' ', end='')
