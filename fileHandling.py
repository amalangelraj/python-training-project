with open("D:/pythoncourse/filehandling/text.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")



f = open("D:/pythoncourse/filehandling/text.txt",'r',encoding = 'utf-8')
f.read(4)    # read the first 4 data
f.read(4)    # read the next 4 data
f.read()     # read in the rest till end of file 'my first file\nThis file\ncontains three lines\n'
f.read()  # further reading returns empty sting


text = "This is new content"
# writing new content to the file
fp = open("D:/pythoncourse/filehandling/text.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()


# Python code to illustrate with() alongwith write()
with open("D:/pythoncourse/filehandling/text.txt", "w") as f:
    f.write("Hello World!!!")
