# 1.4 Multidimensional Lists

[Back to chapter overview](../README.md)

[< back](./3-local-global.md) ---
[next >](./5-file-handling.md)

---

## 1D-Lists

You've seen one dimensional lists before. They are very useful to store data in variables and they are easy accessible. You can save any type of data in lists like numbers, booleans or strings. There are many helper functions to manipulate those lists (slice, pop, remove,...)

```python
one_dimension_list = [1,2,3,4,5]
print(one_dimension_list[1]) # prints 2 (second element)
one_dimension_list[-1] = 100 # overwrites last element
```

## 2D-Lists

Lists are not only good to store numbers or strings in lists, you can even store lists in lists to store two dimensional data. That helps for example if you want to implement a tictactoe game in python (see notes folder) or for any other 2D implementation.

```python
two_dimensions_list = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
print(two_dimensions_list[1]) # prints seconds row
print(two_dimensions_list[1][0]) # prints first item of seconds row
two_dimensions_list[-1][3] = 100 # overwrites fourth element of last row
```

## nD-Lists

There are almost no limits of how many dimensions you want to store in lists.
But be aware to keep track of the formatting of your code. The more dimensions and items in a list you have, the harder it gets to read and understand.

## Looping through dimensions

Also the iterating through these data structures is similar to one dimensional lists:

```python
one_dimension_list = [1,2,3,4,5]

for item in one_dimension_list: # note: you can choose your own variable name instead of item
    print(item)

two_dimensions_list = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]

for row in two_dimensions_list: # note: you can choose your own variable name instead of row and item
    for item in row:
        print(item)
```

---

[Back to chapter overview](../README.md)

[< back](./3-local-global.md) ---
[next >](./5-file-handling.md)
