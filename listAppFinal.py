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
    6. Recursive binary search
    7. Iterative binary search
    8. Print contents of list
    9. Quit program   """)
            """

            This is a very basic choice system, where your input
            determines what function is ran.

            """
            if choice == '1':
                addToList()
                sortList(myList)
            elif choice == '2':
                addABunch(myList)
            elif choice == '3':
                indexValues()
            elif choice == '4':
                randomSearch()
            elif choice == '5':
                linearSearch()
            elif choice == '6':
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == '7':
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result)) 
                else:
                    print("Your number could not be found in the list")
            elif choice == '8':
                printLists()
            else:
                break
        except:
            print("You found a error! Uh oh.")
        #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition
    """

    addToList is a function that adds one number to myList, while addABunch adds as many numbers as the user wants, in any range the user wants.

    """
def addToList():
    print('Adding to a list! Great choice!')
    newItem = input('Type a new integer here!   ')
    myList.append(int(newItem))

def addABunch(myList):
    try:
        print("We're gonna add a bunch of integers here!")
        numToAdd = input("how many integers to add?   ")
        numBottomRange = input("How low would you like the numbers to go?   ")
        numTopRange = input("And how high would you like those numbers to go?   ")
        for x in range (0, int(numToAdd)):
            myList.append(random.randint(int(numBottomRange), int(numTopRange)))
        print("Your list is now complete.")
        print("Sorting your data...")
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
    except:
        print("Your bottom range must be lower than your top range.")
    """

    indexValues is a function that will search myList for the number you specify and tell you it's index location.
    sortList is a function that will search your list for unique variables and add them to unique_list, creating a list consisting of only unique variables
    
    """
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
    """

    randomSearch is a function that will randomly give you a variable from myList.
    linearSearch is a function that will search each item in myList for the specified variable.

    """
def randomSearch():
    print("Random search time!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list!")
    searchItem = input("What're you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

    """

    recursiveBinarySearch and iterativeBinarySearch both split unique_list into to the top and bottom parts of the list, then determines
    if the chosen number is above or below the middle number. the difference is that recursiveBinarySearch calls itself to repeat, while
    iterativeBinarySearch uses a while statement to repeat it's code repeatedly until the correct number is found.

    """
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)
        else:
            recursiveBinarySearch(unique_list, mid +1, high, x)
    else:
        print("Your number isnt here!")
        
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        
        if  unique_list[mid] < x:
            low = mid +1
        elif unique_list[mid] > x:
            high = mid -1
        else:
            return mid
    return -1

    """

    the printLists function allows the user to decide which list to print, and prints the list specified.
    the dunder main statement does something, i dont know what though

    """
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
