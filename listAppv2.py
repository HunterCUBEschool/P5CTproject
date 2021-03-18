"""

program goals
get inputs from user (at multiple points)
we need to convert some of thi input to ints from strs
we need to provide choices to user
    add more values to list
    return a value at a specific index

"""
import random

myList = []
def mainProgram():
    while True:
        print("Hello, there! Let's work with lists!")
        print("Choose from the following options. Type a number below!")
        choice = input("""1. Add to a list ,
    2. Add a bunch of numbers t a list
    3. Return the value at an index position
    4. Random search
    5. Print contents of list
    6. Quit program""")
        if choice == '1':
            addToList()
        elif choice == '2':
            addABunch()
        elif choice == '3':
            indexValues()
        elif choice == '4':
            randomSearch()
        elif choice == '5':
            print(myList)
        else:
            break
        #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition
    
def addToList():
    print('Adding to a list! Great choice!')
    newItem = input('Type a new integer here!   ')
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("how many integers to add?   ")
    numRange = input("And how high would you like those numbers to go?   ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")
    
def indexValues():
    print("Loading up your list now")
    indexPos = input("Which data piece would you like to see?    ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Random search time!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! this sucks.")
    searchItem = input("What're you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position ()".format(x))
    

if __name__ == "__main__" :
    mainProgram()
