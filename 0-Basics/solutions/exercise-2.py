# 1

name = input("Whats your name? ")
age = int(input("How old are you? "))
print("Which are your favourite movies? ")
movies = []
movies.append(input("1: "))
movies.append(input("2: "))
movies.append(input("3: "))
python_skills = float(
    input("How do your rate your python skills (0.0-10.0)? "))
hasPetsInput = input("Do you have pets? (y/n)")
if hasPetsInput == "y":
    hasPets = True
else:
    hasPets = False

print(name, type(name))
print(age, type(age))
print(movies, type(movies[0]))
print(python_skills, type(python_skills))
print(hasPets, type(hasPets))


# 2
# a
sum = 0
for i in range(100+1):
    sum += i
    print(i)
print(sum)

# b
for i in range(100+1):
    if i % 2 == 0:
        print(i)

# b
for i in range(100+1):
    if i % 2 == 0 and i % 4 != 0:
        print(i)

# c
for i in range(100+1):
    isPrime = True
    if i < 2:
        isPrime = False
    for j in range(2, i):
        if j != 0 and i % j == 0:
            isPrime = False

    if isPrime:
        print("prime", i)

# 3
iterations = 5
mistakes = 0
task_solved = False
print("Write the following sentence for " + str(iterations) + " times:")
print("I enjoy learning Python with Jakob")

while not task_solved:
    for i in range(iterations):
        inputString = input(str(i) + ": ")

        if inputString != "I enjoy learning Python with Jakob":
            mistakes += 1
            print("Wrong, try again")
            print("")
            print("")
            break
        elif i == iterations - 1:
            task_solved = True

print("Congratulations, you made it!")
print("You made " + str(mistakes) + " mistakes")
