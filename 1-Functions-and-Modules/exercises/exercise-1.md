# 1.1 Sum, Factorial, Fibonacci functions

Ask the user for a number n and calculate the sum from 1 to n, n! (factorial) and fibonacci(n). Implement functions for these calculations and use the following code as a starting point:

```python
userInput = int(input("Enter a number: "))                  # example: 7
print(f"Sum [1, {userInput}] = {sum(userInput)}")           # result: 28
print(f"{userInput}! = {factorial(userInput)}")             # result: 5040
print(f"fibonacci({userInput}) = {fibonacci(userInput)}")   # result: 13
```

# 1.2 Functions for lists

Write functions to calculate the min, max and average value of a given list with numbers (int or floats).
Use the following code as a starting point:

```python
myList = [-3, -.4, 0, 2, 3.14, 8.4, 15]
print(f"minList(myList) = {minList(myList)}")           # result: -3
print(f"maxList(myList) = {maxList(myList)}")           # result: 15
print(f"sumList(myList) = {sumList(myList)}")           # result: 25.14
print(f"avgList(myList) = {avgList(myList)}")           # result: 3.59...
```

# 1.3 Temperature conversion Celsius <=> Fahrenheit

Convert the temperature from celsius to fahrenheit depending on the user input. Your program should accept "C", "c", "Celsius", "celsius", "F", "f", "Fahrenheit", "fahrenheit" as input.

```python
inputTemperature = int(input("Temperature: ")) # example: 29
inputUnit = input("Celsius / Fahrenheit: ") # example: C

print(f"{inputTemperature}° {inputUnit} <=> {round(convertTemperature(inputTemperature, inputUnit),2)}° {convertUnit(inputUnit)}")
# returns: 29° C <=> 84.2° F
```
