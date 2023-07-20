# 0.2 Lists

[Back to chapter overview](../README.md)

[< back](2-variables.md) ---
[next >](4-loops-and-conditions.md)

---

Lists can store multiple variables in an array. The first index is 0 and you can store as many values as you want. Values are separated by a `,`.
Note that it is possible to store the same value multiple times. If you want to have a list with unique values use a set.

To avoid exceptions always make sure you don't try to access values that not exist. The maximum index is len()-1

```python
shopping_list = ["apples", "bananas", "lemons", "beer", "tomatoes"]

print(len(shopping_list)) # length of list
print(shopping_list[2]) # get value of 3rd item in list
shopping_list.append("bread") # add a new value to list
shopping_list.remove("apples") # removes specific value
shopping_list.pop(0)  # remove item at index 0
```

Once a value is set you can edit it later

```python
shopping_list[0] = "green apples"
```

If you only have enough space in your shopping cart for 2 items of your list you can access them separately

```python
print(shopping_list[:2]) # first 2 items
print(shopping_list[len(shopping_list)-2:]) # last 2 items
print(shopping_list[2:4]) # 3rd, 4th item
```

---

[Back to chapter overview](../README.md)

[< back](2-variables.md) ---
[next >](4-loops-and-conditions.md)
