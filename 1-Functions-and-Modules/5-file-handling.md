# 1.5 File Handling

[Back to chapter overview](../README.md)

[< back](./2-random.md) ---
[next >](./4-multidimensional-lists.md)

---

Until now we let the user type in some input before we started our calculations in the exercises. Let's assume you want to process a lot of data and there are too many data entries to type them all in. How can we read in data to python?

Or imagine you did some complex calculations in your python program and want to save the result in the end. Or you implemented a small game and want to save the progress within the game to continue playing later. How can you persist data in python?

## Files

There are many differenty ways to import and export data to python. We will start with files. For unstructured data and text we can use .txt files and for structured data we can read in .csv files (comma separated value). You can see examples in the notes folder.

## Read in files

You can open files with the following commands:

```python
# txt file
with open('example.txt', 'r') as file: # filename and file mode
    content = file.read() # reads the entire content
    lines = file.readlines() # reads the content line by line


import csv
data = []
with open('data.csv', 'r') as file: # filename and file mode
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row) # save content of csv file line by line and add to data variable
```

There are different modes to open a file:

- r: read
- w: write (overwrites file, carefull!)
- a: append (add content at the end of the file)

## Write files

The structure is similiar to reading files but you have to change the mode to w/a and use different functions provided by python / csv-module:

```python
# txt file
with open('example.txt', 'w') as file: # filename and file mode
    file.write('new content') # write to file


import csv
with open('data.csv', 'w', newline='') as file: # filename and file mode
    # Open and write to a CSV file
    csv_writer = csv.writer(file)

    # Write rows to the CSV file
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Alice', 25])
    csv_writer.writerow(['Bob', 30])
```

---

[Back to chapter overview](../README.md)

[< back](./2-random.md) ---
[next >](./4-multidimensional-lists.md)
