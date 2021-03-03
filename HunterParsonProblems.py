"""
March 2, 2021

Use this document to record your answers to the Parson's Problems
shared in class.

Remember: the idea behind a Parson's Problem is that you are
shown completely correct code that is presented OUT OF ORDER.
When arranged correctly, the code does what the Parson's Problem
says it should do.

"""


#Write your answer to Parson's Problem #1 below:
for x in (1,1,1,1,1,1,1,1,1,1):
    print('hello world')
#Write your answer to Parson's Problem #2 below:
myList = []
myList.append("apples")
myList.append("pineapples")
print(myList)
#Write your answer to Parson's Problem #3 below:

try:
    x = input("Type a number ")
    print("That's more than nothing!")
    x = int(x)
 
    if x > 0:

        print("Wow,", x ,"is a great number!")

    else:
        print("That's not a number!")

except ValueError:
    print("That's not a number!")
