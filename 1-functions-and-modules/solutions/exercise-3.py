# --- 3.1 ---
# days to seconds

while True:
    userInput = input("How many days? (Type exit to end program) ")
    if userInput == "exit":
        break
    userInput = int(userInput)

    seconds = userInput * 24 * 60 * 60

    print(f"{userInput} days are {seconds} seconds")

# --- 3.2 ---
# 7464643 seconds to mars

while True:
    userInput = input("How many seconds? (Type exit to end program) ")
    if userInput == "exit":
        break
    userInput = int(userInput)

    years = userInput // (365*24*60*60)
    days = (userInput // (24*60*60)) % 365
    hours = (userInput // (60*60)) % 24
    minutes = (userInput // (60)) % 60
    seconds = userInput % 60

    print(f"{userInput} seconds are {years} year(s), {days} day(s), {hours} hour(s), {minutes} minute(s) and {seconds} second(s).")


# --- 3.3 ---
# Vowel Counter

userInput = input("Type in a sentence ")
vowel_counter = 0
password = ""

# solution #1
for char in userInput:
    if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
        vowel_counter += 1
    else:
        if char == " ":
            password += "%"
        else:
            password += char

print("Solution #1")
print(f"Sentence: {userInput}")
print(f"{vowel_counter} vowels")
print(f"Password: {password}")

# solution #2
vowel_counter = 0
password = ""

userInputWithReplacements = userInput.replace(" ", "%")
vowels = ["a", "e", "i", "o", "u"]

for char in userInput:
    if char.lower() in vowels:
        vowel_counter += 1
    else:
        password += char


print("Solution #2")
print(f"Sentence: {userInput}")
print(f"{vowel_counter} vowels")
print(f"Password: {password}")


# solution #3
print("Solution #2")
print(f"Sentence: {userInput}")
print(next(map(lambda x: (
    sum(1 for char in x if char.lower() in 'aeiou'), x.replace(' ', '%')), [userInput])))


# --- 3.4 ---
# sum to user number
x = int(input("x "))
y = int(input("y "))
sum = 0
for i in range(0, x):
    sum += i
    if i % y == 0:
        print(i)

print("sum:", sum)

# --- 3.5 ---
# factorial

userInput = int(input("What's your number? "))
fac = 1
for i in range(1, userInput+1):
    fac *= i
print("factorial:", fac)

# --- 3.6 ---
# fibnonacci

userInput = int(input("What's your number? "))
fibonacci = []
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
for i in range(0, userInput+1):
    if len(fibonacci) >= 2:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    else:
        fibonacci.append(i)

    print(f"{i}. fibonacci: {fibonacci}")
