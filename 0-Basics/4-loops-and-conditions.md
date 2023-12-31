# 0.4 loops and conditions

[Back to chapter overview](../README.md)

[< back](3-lists.md) ---
[next >](5-mathematical-operators.md)

---

## if statement

To execute commands only in certain conditions you can use if statements. It checks the value of the condition and executes the following intended code lines when the condition is true.
You can also provide an optional else block or even add more if conditions in an else if (elif in python) statement.

```python
age = 14

if age < 3:
    print("free time")
elif age < 6:
    print("kindergarten")
elif age < 18:
    print("school")
elif age < 25:
    print("university")
elif age > 65:
    print("free time")
else:
    print("work")
```

## Loops

### For

If you want to iterate through a list, you can use a for-loop:

```python
shopping_list = ["apples", "bananas", "lemons", "beer", "tomatoes"]
for item in shopping_list:
    print(item)
```

It's also possible to create loops which runs for x-times

```python
for i in range(10):
    print(i)
```

You can use the range function to fill a list with new items:

```python
myList = []
for i in range(10):
    myList.append(i)
```

To exit the loop before you reached the last value, add a `break` command:

```python
for item in shopping_list:
    if item == "broccoli":
        break # if you don't like broccoli
```

### While

In addition to for-loops you can also iterate until a certain condition is reached:

```python
space_in_shoppingcart = 4
while space_in_shoppingcart > 0:
    continueShopping()
    space_in_shoppingcart -= 1
```

## Conditions

If you want to run specific commands based on a condition, you can use if-statements

```python
for i in range(10):
    if i % 2 == 0: # modulo operator (returns the integer remainder of division)
        print("even")
    else:
        print("odd")
```

## Boolean expressions

In the previous examples you have already seen some basic decisions made on conditions, for example if you want to continue with the for-loop or while-loop.

Typical expressions are:

- == Equal to
- != Not equal to
- < Less than
- \> Greater than
- <= Less than or equal to
- \>= Greater than or equal to
- and: True if both operands are true
- or: True if at least one operand is true
- not: True if the operand is false (inverts the truth value)
- in: True if the first operand is present in the second operand (e.g., in a list, string, or dictionary)
- not in: True if the first operand is not present in the second operand
- is: True if both operands refer to the same object in memory
- is not: True if both operands do not refer to the same object in memory

---

[Back to chapter overview](../README.md)

[< back](3-lists.md) ---
[next >](5-mathematical-operators.md)
