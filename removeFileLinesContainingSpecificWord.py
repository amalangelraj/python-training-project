import os

with open("D:/pythoncourse/filehandling/text.txt", "r") as input:
    with open("D:/pythoncourse/filehandling/temp.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if "word" not in line.strip("\n"):
                output.write(line)

# replace file with original name
os.replace('D:/pythoncourse/filehandling/temp.txt', 'D:/pythoncourse/filehandling/text.txt')
