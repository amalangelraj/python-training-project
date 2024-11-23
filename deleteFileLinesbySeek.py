with open(r"D:/pythoncourse/filehandling/text.txt", 'r+') as fp:
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines
    # iterate line and line number
    for number, line in enumerate(lines):
        # delete line number 5 and 8
        # note: list index start from 0
        if number not in [4, 7]:
            fp.write(line)
