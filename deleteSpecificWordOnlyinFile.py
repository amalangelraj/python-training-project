import os

original_file = "D:/pythoncourse/filehandling/text.txt"
temp_file = "D:/pythoncourse/filehandling/temp.txt"

string_to_delete = ['Emma', 'Kelly']
with open(original_file, "r") as input:
    with open(temp_file, "w") as output:
        for line in input:
            for word in string_to_delete:
                line = line.replace(word, "")
            output.write(line)

# replace file with original name
os.replace('D:/pythoncourse/filehandling/temp.txt', 'D:/pythoncourse/filehandling/text.txt')
