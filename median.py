"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

mean = 0
numbersLen = len(numbers)
numbers.sort()
if numbersLen > 0:
    if numbersLen % 2 == 0:
     mean = (numbers[numbersLen//2] + numbers[numbersLen//2-1]) /2
    else:
         mean = numbers[numbersLen//2]
else: 
    mean = numbers[numbersLen]
print(mean)