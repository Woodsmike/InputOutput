# jabber = open("/Users/mgwwl/Desktop/Code.txt",'r')
#
# for line in jabber:
#     if "Withdraw" in jabber:
#         print(line, end= ' ')
#
# jabber.close()

# with open("Code.txt", 'r') as jabber:
#     for line in jabber:
#         if "withdraw" in line.lower():
#             print(line, end= ' ')
#
# with open("Code.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end= ' ')
#         line = jabber.readline()

# -----return a list of lines to be processed------

# with open("Code.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("Code.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("Code.txt", 'r') as jabber:
    lines = jabber.read()  # used mainly in binary files
print(lines)

for line in lines[::-1]:
    print(line, end='')