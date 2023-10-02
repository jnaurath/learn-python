# Open and read a text file
import csv
with open('example.txt', 'r') as file:
    content = file.read()  # Read the entire content into a string
    # Alternatively, you can read line by line:
    # line = file.readline()
    # lines = file.readlines()

# Print the content
print(content)


# Open and write to a text file
with open('example.txt', 'w') as file:  # a: append
    file.write('This is a line of text.\n')
    file.write('Another line of text.\n')


# Open and append lines to a text file
with open('example.txt', 'a') as file:  # a: append
    file.write('You can also add new lines.\n')
    file.write('Make sure to use mode a for append.\n')


# Open and read a CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        # 'row' is a list containing the values from one row of the CSV
        print(row)


# Open and write to a CSV file
with open('data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    # Write rows to the CSV file
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Alice', 25])
    csv_writer.writerow(['Bob', 30])


# Open and append data to a CSV file
with open('data.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)

    # Write rows to the CSV file
    csv_writer.writerow(['George', 52])
    csv_writer.writerow(['Hermine', 3])
