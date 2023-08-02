# expressions and boolean operators

print(True == True)  # True
print(True != True)  # False
print(3 == 4)       # False
print(3 < 4)        # True
print(3 > 4)        # False
print(3 <= 4)       # True
print(3 >= 4)       # False
print(4 <= 4)       # True
print(4 >= 4)       # True


# AND: True if both / all operands are true
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# OR: True if at least one operand is true
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

print(True and True or False)   # True
print(False and True or True)   # True
print(False and True and True)   # False
print(False or True and True)   # True
print(False or False or False or False or False or False or False or False or False or True)   # True

# combination
print(True and True)    # True
print(3 < 4 and 4 >= 4)    # True
print(3 < 4 and 4 >= 4)    # True

# example
name = "Hans"
age = 0
startYear = 2023
currentYear = 2023

minimalPensionAge = 67

print("We welcome our little", name, "geboren", startYear)

for i in range(101):
    print("Iteration:", i, "Year:", currentYear)

    if age >= minimalPensionAge:
        print(name, "receives a pension")
    else:
        print(name, "keep working!")

    age += 1
    currentYear += 1

print()
print("RIP", name, ":(")
print(startYear, "-", currentYear)
