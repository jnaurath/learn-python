name = "Hans"
age = 28

# adds a whitespace between strings and values
print("Hello, my name is", name, "I'm", age, "years old")

# you have to convert the type of the variable to string
print("Hello, my name is " + name + " I'm " + str(age) + " years old")

# good solution: easy to write, readable and automatic type management
print(f"Hello, my name is {name} I'm {age} years old")
# don't forget "f" before!
print("Hello, my name is {name} I'm {age} years old")  # wrong!!!
