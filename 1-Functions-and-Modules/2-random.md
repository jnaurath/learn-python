# 1.2 Random

[Back to chapter overview](../README.md)

[< back](./1-how-to-find-errors-in-my-code.md) ---
[next >](../README.md)

---

## import modules

You don't have to write every function yourself. There are several modules for many usecases you can import.
Many of them are already included in the standard python library, others you have to install with the pip-package manager.

To import these modules add `import modulename` on the top of your file.

## random-module

One of the standard modules is the random module. Import it with `import random`. It gives you different functions to calculate random numbers.

For example:

```python
random.random() # returns a random float value between 0 and 1
random.randint(lowerInt, upperInt)  # returns a random int value between lowerInt and upperInt (inclusive)

print(random.randint(1, 6)) # dice

```

---

[Back to chapter overview](../README.md)

[< back](./1-how-to-find-errors-in-my-code.md) ---
[next >](../README.md)
