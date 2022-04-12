import math 
# import library for square root

number = input("Enter your number to be analized: ")
number = int(number)
# User input 1

denominator = input("Enter your denominator: ")
denominator = int(denominator)
# User input 2

addition = number + denominator
subtraction = number - denominator
multiply = number * denominator
power = number ** denominator
square_root = power ** (1./ denominator)
quotient = number / denominator
floor = number // denominator
remainder = number % denominator


print ("Addition =", addition)
print ("Subtraction =", subtraction)
print ("Multiplication =", multiply)
print ("Power =", power)
print (denominator,"√", power, " = ", square_root) #Gets the n-root of the exponent
print ("Quotient =", quotient)
print("Floor =", floor)
print("Remainder =", remainder)