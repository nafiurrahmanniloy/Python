# import math
# print(dir(math))
# from math import * to import all the functions
from math import sqrt
print(sqrt(16))

# user define function

# def function_name(parameters):
# do something

# sum of two number function
print("Doing Function things....")


def print_sum(first, second=4):
    sum = first+second
    print(sum)


print_sum(1, 6)  # if we don't initialize 6 then default it will take 4S
