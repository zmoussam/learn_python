fd = open("Lists.py", "r")
print(fd.readable())
# print(fd.read())
print(fd.readline(), end='')
print(fd.readlines()[0])
fd.close()