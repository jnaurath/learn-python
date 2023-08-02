# math
sum = 0
value1 = 1
value2 = 3

# +
print(1 + 3)

sum = 1 + 3
print(sum)

# 4   = 1     + 3     + 0
sum = value1 + value2 + sum
# 8   = 1     + 3     + 4
sum = value1 + value2 + sum
sum = sum + value1 + value2
sum += value1 + value2

print(value1+value2)
print(sum)

# -
sum = value1 - value2  # 1 - 3 = -2
print(sum)

# *
sum = value1 * value2  # 1 * 3 = 3
print(sum)

# /
# 0 = 1 / 3         Integer
# 0.0 = 1.0 / 3.0   Float
sum = value1 / value2  # 1 / 3 = .3333 Float
print(sum)

sum = value1 // value2 + 1  # 1 / 3 = 0 rounded down to nearest integer!
print(sum)

print(round(sum, 2))

sum = 12 // 7 + 1
print(sum)

# warning: division 0! -> ZeroDivisionError
# print(0/0)

# % Modulo division with remainder
# 12 / 7 = 1, remainder 5
print(12 % 7)  # 5

print(12 % 2)  # 5

# exponentiation
print(2**2)  # 2^2
print(4**-2)  # 2^(-2)
print(4**(1/2))  # 2^(1/2) --> square root
print(2**4)  # 2^4
print((3**2)**2*3)  # 2^4


# ordering:
# 1. **
# 2. * / %
# 3. + -

# otherwise use ()
print((3+2)*4)

print("#######")
print(3+4*5)  # returns
print((3+4)*5)  # returns
print(3+4**2)  # returns
print((3+4)**2)  # returns
print("#######")

print(12 % 7)  # 1, remainder 5

print(1 % 4)  # 0, remainder 1
print(2 % 4)  # 0, remainder 2
print(3 % 4)  # 0, remainder 3
print(4 % 4)  # 1, remainder 0
print(5 % 4)  # 1, remainder 1

print(3 * 10 % 3)
