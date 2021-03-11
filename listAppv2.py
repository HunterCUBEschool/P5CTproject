"""

program goals
get inputs from user (at multiple points)
we need to convert some of thi input to ints from strs
we need to provide choices to user
    add more values to list
    return a value at a specific index

"""

myList = []
def mainProgram():
    while True:
        print("Hello, there! Let's work with lists!")
        print("Choose from the following options. Type a number below!")
        choice = input("""1. Add to a list ,
    2. Return the value at an index position
    3. Exit Program     """)
        if choice == '1':
            addToList()
        elif choice == '1':
            indexValues()
        elif choice == '3':
            break
        #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition
    
def addToList():
    print('Adding to a list! Great choice!')
    newItem = input('Type a new integer here!   ')
    myList.append(int(newItem))
def indexValues():
    print("Loading up your list now")
    indexPos = input("Which data piece would you like to see?    ")
    print(myList[int(indexPos)])

                                
if__name__=="__main__"
    mainProgram()
