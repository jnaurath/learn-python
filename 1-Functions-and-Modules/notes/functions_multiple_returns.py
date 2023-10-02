def myFunction(x_local, y_local):
    x_local += 10
    y_local += 10
    print(x_local)
    print(y_local)
    return x_local, y_local


x = 2
y = 3
print(x)
print(y)
print("----")

x, y = myFunction(x, y)

print("----")

print(x)
print(y)
