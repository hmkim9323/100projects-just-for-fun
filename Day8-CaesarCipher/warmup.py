"""
import math

# Area Calc
given_h = int(input("Height of the wall: "))
given_w = int(input("Width of the wall: "))

coverage = 5

def paint_calc(given_h, given_w, coverage):
    number_of_cans = math.ceil((given_h * given_w) / coverage)

    print(f"You'll need {number_of_cans} cans of paint.")

paint_calc(given_h, given_w, coverage)


def prime_checker(number):

    if number == 1:
        print("It's not a prime number.")
        return False

    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return False

    print("It's a prime number.")
    return True

n = int(input("Check this number: "))
prime_checker(number=n)
"""