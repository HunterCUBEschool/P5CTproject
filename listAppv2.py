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
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""    1. Add to the list ,
    2. Add a bunch of numbers to the list
    3. Return the value at an index position
    4. Random search
    5. Linear search
    6. Sort list
    7. Print contents of list
    8. Quit program   """)
            if choice == '1':
                addToList()
            elif choice == '2':
                addABunch()
            elif choice == '3':
                indexValues()
            elif choice == '4':
                randomSearch()
            elif choice == '5':
                linearSearch()
            elif choice == '6':
                sortList(myList)
            elif choice == '7':
                printLists()
            else:
                break
        except:
            print("You found a error! Uh oh.")
        #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition
    
def addToList():
    print('Adding to a list! Great choice!')
    newItem = input('Type a new integer here!   ')
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("how many integers to add?   ")
    numBottomRange = input("How low would you like the numbers to go?   ")
    numTopRange = input("And how high would you like those numbers to go?   ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(int(numBottomRange), int(numTopRange)))
    print("Your list is now complete.")
    
def indexValues():
    print("Loading up your list now")
    indexPos = input("Which data piece would you like to see?    ")
    print("Your search came up with {}".format(myList[int(indexPos)]))

def sortList(myList):
    print("Sorting your data...")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N   ")
    if showMe.lower() == "y":
        print (unique_list)

def randomSearch():
    print("Random search time!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! this sucks.")
    searchItem = input("What're you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid - (high + low) // 2
    else:
        print("Your number isnt here!")
            
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
    

if __name__ == "__main__" :
    mainProgram()
