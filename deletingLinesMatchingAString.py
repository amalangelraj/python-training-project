with open("D:/pythoncourse/filehandling/text.txt", "r") as fp:
    lines = fp.readlines()

with open("D:/pythoncourse/filehandling/text.txt", "w") as fp:
    for line in lines:
        if line.strip("\n") != "text to delete":
            fp.write(line)
