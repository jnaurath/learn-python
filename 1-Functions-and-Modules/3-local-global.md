# 1.3 Local and Global variables

[Back to chapter overview](../README.md)

[< back](./2-random.md) ---
[next >](./4-multidimensional-lists.md)

---

## differences

When your program gets more complex over time and you write multiple functions to avoid rewriting your functionality you need to understand the scope of the defined variables.

If you define your variable outside of functions on the base level, these variables become global. You can use them on the same level and even inside other functions. But keep in mind that you can't change their value later inside of a function. Therefore you need to add the keyword 'global' inside your function.

```python
x = 10 # global

print(x) # prints 10, same level as global variable

x += 1 # changes the value of your variables, same level as global variable declaration

def myFunctionERROR():
    print(x) # prints 11, you can read the global values even inside functions
    x += 1 # ERROR: you can't change the value

def myFunction():
    global x # use global keyword
    print(x) # prints 11, you can read the global values even inside functions
    x += 1 # changes the value of your variables
```

## return value from function

Variables declared inside a function are local and can't be read or changed by other functions. If you want to share the value of a variable without declaring it as a global variable you can return it in the end of your function:

```python
def myFunctionWithoutReturn():
    name = "Greta" # definition of a local variable

print(name) # Error: you can't read the values of local variables


def myFunctionWithReturn():
    name = "Greta" # definition of a local variable
    return name

print(myFunctionWithReturn()) # prints the value of name because it's returned by the function
name = myFunctionWithReturn() # you can also save the return value in a new variable on a global level
```

## multiple return values

In case you need to return multiple values you can write your functions definitions like this:

```python
def myFunction():
    name = "Greta" # definition of a local string
    age = 12 # definition of a local int
    hasDriversLicense = False # definition of a local boolean
    return name, age, hasDriversLicense # returns all local variables


name, age, hasDriversLicense = myFunction() # saves multiple return values
```

## best practice

It's recommended to use as few global variables or global statements in your functions as possible. The idea of functions is to execute the same logic without any side effects like changing too many global variables. By doing so your program get's more readable, predictable and reusable for many other use cases.

---

[Back to chapter overview](../README.md)

[< back](./2-random.md) ---
[next >](./4-multidimensional-lists.md)
