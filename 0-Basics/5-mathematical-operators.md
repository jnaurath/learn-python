# 0.5 Mathematical Operators

[Back to chapter overview](../README.md)

[< back](4-loops-and-conditions.md) ---
[next >](exercises/exercise-1.md)

---

## List of operators

```python
# Addition
result = 5 + 3  # Output: 8
# Subtraction
result = 10 - 4  # Output: 6
# Multiplication
result = 2 * 6  # Output: 12
# Division
result = 20 / 5  # Output: 4.0 (floating-point division)
# Floor Division
result = 20 // 3  # Output: 6 (floor value of the division)
# Modulus
result = 17 % 5  # Output: 2 (remainder of 17 divided by 5)
# Exponentiation
result = 2 ** 3  # Output: 8 (2 raised to the power of 3)
```

## Ordering

1. Exponentiation: \*\*
2. Multiplication, division, and modulo: \*, /, %
3. Addition and subtraction: +, -

If you want to calculate in a different order, make sure to use `()`. Example:

```python
print(3+4*5)    # 23
print((3+4)*5)  # 35
print(3+4**2)   # 19
print((3+4)**2) # 49
```

---

[Back to chapter overview](../README.md)

[< back](4-loops-and-conditions.md) ---
[next >](exercises/exercise-1.md)
