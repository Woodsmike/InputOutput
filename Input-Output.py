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
# ----------------------

# with open("Code.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')
#
# with open("Code.txt", 'r') as jabber:
#     lines = jabber.read()  # used mainly in binary files
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

# ------write a file------
# cities = ["Atlanta", "Melbourne", "Jackson", "Sydney", "Darwin"]
#
# with open("cities.txt", 'w') as cityFile:
#     for city in cities:
#         print(city, file=cityFile)
#
# cities = []
# with open("cities.txt", 'r') as cityFile:
#     for city in cityFile:
#         cities.append(city.strip('\n'))  # strip only removes ending/beginning letters
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"),(2, "Pscyho"),(3, "Mayhem"),(4, "Kentish Town Waltz"))
#
# with open("Imelda3.txt", 'w') as imeldaFile:
#         print(imelda, file=imeldaFile)

# with open("Imelda3.txt", 'r') as imeldaFile:
#     contents = imeldaFile.readline()
#
# imelda = eval(contents)
#
# print(imelda)

# challenge --- write a program to append the times table to the cities file in Code.txt.  We want the tables
# fromm 2 to 12.  The first column of numbers should be right justified.

with open("cities.txt",'a') as cityFile:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=cityFile)
print(cityFile)