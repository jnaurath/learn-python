# 1.0 Function declaration

[Back to chapter overview](../README.md)

[< back](../0-Basics/5-mathematical-operators.md) ---
[next >](./1-how-to-find-errors-in-my-code.md)

---

## Why functions?

If you want to reuse your code snippets and run it multiple times it's easier and more readable to create functions.
Once written you can call them from anywhere in your code and your codes get's easier to read.
To declare functions you have to use the following structure:

```python
def my_function():
    print("Hello, I'm a python function")
```

To run the code blocks within you can call it from anywhere in your code with

```python
my_function() # prints "Hello, I'm a python function"
```

## Arguments

You can also pass arguments to the function to do some calculations or use these values within the functions. If you want to use multiple arguments, seperate the with a comma and use good names for these variable to keep track of them.

```python
# function to say hello
def sayHello(name):
    print(f"Hello {name}, how are you?")

sayHello("Peter")


# function to add numbers
def addTwoNumbers(number1, number2):
    sum = number1 + number2
    print(f"{number1} + {number1} = {sum}")

addTwoNumbers(2,5) # result: 7
```

## return value from function

To do some calculation inside a function and use the calculated value again you can return the result from the function

```python
# function to add numbers
def addTwoNumbers(number1, number2):
    return number1 + number2

# function to multiply numbers
def multiplyTwoNumbers(number1, number2):
    return number1 * number2

result = addTwoNumbers(2,5) # result: 7
result = multiplyTwoNumbers(result, 2) # result: 14
```

---

[Back to chapter overview](../README.md)

[< back](../0-Basics/5-mathematical-operators.md) ---
[next >](./1-how-to-find-errors-in-my-code.md)
