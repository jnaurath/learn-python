# task 1

chatbot = [
    "How are you? ",
    "What's your name? ",
    "Where do you live? ",
    "How old are you? ",
    "What's your favorite food? ",
]

answers = []

# print question and read user input # save user input in list
antwort0 = input(chatbot[0])
answers.append(input(chatbot[0]))
answers.append(input(chatbot[1]))
answers.append(input(chatbot[2]))
answers.append(input(chatbot[3]))
answers.append(input(chatbot[4]))


# or iterate through list with for-loop to save many line of code
for question in chatbot:
    answers.append(input(question))


print(answers)


# task 2

shopping_bag = []
shopping_list = []

shopping_list.append("Pizza")
shopping_list.append("Coke")
shopping_list.append("Salt")
shopping_list.append("Pepper")
shopping_list.append("Apple")
shopping_list.append("Banana")

shopping_list.remove("Coke")

shopping_list.append("Orange Juice")

print("How many items are currently on my shopping list?")
print(len(shopping_list))

shopping_bag.append(shopping_list[0])

shopping_bag.append(shopping_list[2])

shopping_bag.append(shopping_list[-1])
print(shopping_list)
shopping_list.pop(0)
shopping_list.pop(1)
shopping_list.pop(-1)
print(shopping_list)


print("What is missing?")
print(shopping_list)

shopping_bag += shopping_list
shopping_list.clear()
print(shopping_bag)
shopping_bag = shopping_bag[:-2]

print("What's still in his bag?")
print(shopping_bag)


# list: pizza, coke, salt, pepper, apple, banana
# list: pizza, salt, pepper, apple, banana, orange juice
# list: 6 items
# list: salt, apple, banana
# bag: pizza, pepper, orange juice
# bag: pizza, pepper, orange juice, salt, apple, banana
# bag: pizza, pepper, orange juice, salt
