###### local ######

def my_function():
    x = 10  # This is a local variable
    print(x)


my_function()  # Output: 10
print(x)  # This would result in an error since 'x' is not defined in the global scope


###### global ######
x = 10  # This is a global variable


def my_function():
    print(x)  # Accessing the global variable 'x' from within a function


my_function()  # Output: 10

print(x)  # Accessing the global variable 'x' outside the function


###### modify global ######
x = 10  # This is a global variable


def modify_global():
    global x
    x = 20


modify_global()
print(x)  # Output: 20
