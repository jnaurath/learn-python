import math
import time


def sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def fibonacci_list(n):
    fibonacci = []
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    for i in range(0, n+1):
        if len(fibonacci) >= 2:
            fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
        else:
            fibonacci.append(i)
    return fibonacci[-1]


def fibonacci_recursion(input):
    if input == 0:
        result = 0
    elif input == 1:
        result = 1
    elif input >= 2:
        result = fibonacci_recursion(input-1)+fibonacci_recursion(input-2)
    return result


def fibonacci_function(n):
    a = 1/(math.sqrt(5))
    b = ((1+math.sqrt(5))/2)**n
    c = ((1-math.sqrt(5))/2)**n
    fibonacci = a * (b-c)
    return round(fibonacci)


userInput = int(input("Enter a number: "))                  # example: 7
print(f"Sum [1, {userInput}] = {sum(userInput)}")           # result: 28
print(f"{userInput}! = {factorial(userInput)}")             # result: 5040

start_time = time.time()
# result: 13
print(f"fibonacci_list({userInput}) = {fibonacci_list(userInput)}")
end_time = time.time()
runtime = end_time - start_time
print(f"Function took {round(runtime,2)} seconds to execute.")

start_time = time.time()
print(f"fibonacci_recursion({userInput}) = {fibonacci_recursion(userInput)}")
end_time = time.time()
runtime = end_time - start_time
print(f"Function took {round(runtime,2)} seconds to execute.")

start_time = time.time()
print(f"fibonacci_function({userInput}) = {fibonacci_function(userInput)}")
end_time = time.time()
runtime = end_time - start_time
print(f"Function took {round(runtime,2)} seconds to execute.")


def minList(inputList):
    result = inputList[0]
    for element in inputList:
        if element < result:
            result = element
    return result


def maxList(inputList):
    result = inputList[0]
    for element in inputList:
        if element > result:
            result = element
    return result


def sumList(inputList):
    result = 0
    for element in inputList:
        result += element
    return result


def avgList(inputList):
    return sumList(inputList) / len(inputList)


myList = [-3, -.4, 0, 2, 3.14, 8.4, 15]
print(f"minList(myList) = {minList(myList)}")           # result: -3
print(f"maxList(myList) = {maxList(myList)}")           # result: 15
print(f"sumList(myList) = {sumList(myList)}")           # result: 25.14
print(f"avgList(myList) = {avgList(myList)}")           # result: 3.59...


unitCelsius = ["c", "celsius"]
unitFahrenheit = ["f", "fahrenheit"]


def convertTemperature(temperature, unit):
    if unit.lower() in unitCelsius:
        return temperature * 1.8 + 32
    elif unit.lower() in unitFahrenheit:
        return (temperature - 32)/1.8
    else:
        return "ERROR"


def convertUnit(unit):
    if unit.lower() in unitCelsius:
        return "F"
    elif unit.lower() in unitFahrenheit:
        return "C"
    else:
        return ""


inputTemperature = int(input("Temperature: "))
inputUnit = input("Celsius / Fahrenheit: ")

print(f"{inputTemperature}° {inputUnit} <=> {round(convertTemperature(inputTemperature, inputUnit), 2)}° {convertUnit(inputUnit)}")
