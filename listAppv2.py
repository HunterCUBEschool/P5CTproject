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
    4. Sort list
    5. Random search
    6. Linear search
    7. Recursive binary search
    8. Iterative binary search
    9. Print contents of list
    10. Quit program   """)
            if choice == '1':
                addToList()
            elif choice == '2':
                addABunch()
            elif choice == '3':
                indexValues()
            elif choice =='4':
                sortList(myList)
            elif choice == '5':
                randomSearch()
            elif choice == '6':
                linearSearch()
            elif choice == '7':
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)- 1, int(binsearch))
            elif choice == '8':
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result)) 
                else:
                    print("Your number could not be found in the list")
            elif choice == '9':
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
    print("We're gonna check out each item one at a time in your list!")
    searchItem = input("What're you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid - (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isnt here!")
        
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if  unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


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
