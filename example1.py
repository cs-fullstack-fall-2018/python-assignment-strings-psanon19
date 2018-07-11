# import os
#
# os.system('clear')

bandMate = ("ringo")

# #1.Print the length of the name
# print("The name is this long " , len (bandMate))
#
# #2.Print the name in uppercase, lowercase
# print(bandMate.upper())
# print(bandMate.lower())
#
# #3.Print the middle letter
# print(bandMate[2])
#
# #4.Print the 2nd - 4th letters
# print(bandMate[1:3])
#
# #5.Print the characters to the right of the letter ‘n’
# print(bandMate[4:])
#
# #Challenge A: Discover other object functions and format the name in at least 2 additional ways.
# print(bandMate.capitalize())
# print(bandMate.title())
#
# #Challenge B: Write the code to allow the user to input a name:
# x=input("What is your name?")
# print(x)
#
# #Challenge C: Print “The entered string is x characters long”
# x=input("What is your name?")
# print(x[0:4])
#
# #Challenge D: Print the entered string in a different case (you choose)
# x=input("What is your name?")
# print(x.upper())

# #Challenge E: Enhance the code to allow the user to input multiple names:
# ray=[input("What is your name?"), input("What is your name?"), input("What is your name?"), input("What is your name?")]
# print(ray)

#Challenge F: Print a message about which entered string was longer (the more details the better! Hint: Use print formatting)
ray=[len(input("What is your name?")), len(input("What is your name?")), len(input("What is your name?"))]
print (ray)
if ray[0]>ray[1] and ray[0]>ray[2]:
    print (ray[0], "is the most")
elif ray[1]>ray[0] and ray[1]>ray[2]:
    print (ray[1], "is the most")
elif ray[2]>ray[0] and ray[2]>ray[1]:
    print(ray[2], "is the most")