# function to check if there is a duplicate in the 
def IsDuplicatePresent(theSetOfTasks):
    for task in theSetOfTasks:
            if task == title:
                return True
    return False


# function to check if a list is empty or not
def IsListEmpty(theSetOfTasks):
    if(len(theSetOfTasks) == 0):
        return True
    return False


# main function
try:
    theSetOfTasks = []
    while True:
        print(
        """    Task Manager
        1. Add a new task
        2. Mark a task as completed
        3. View all tasks
        4. Quit
        """)
        val = int(input("Enter your choice: "))
        
        # 1. add new task
        if val == 1:
            title = input("Enter the task name: ")
            # duplicate check
            if IsDuplicatePresent(theSetOfTasks):
                print("Task already exists, try another task!\n")
                continue
            else:
                theSetOfTasks.append(title)
                print(f"Task '{title}' Successfully Added!\n")

        # 2. mark a task as compeleted
        elif val == 2:
            # print and check if any tasks exist in the list
            if IsListEmpty(theSetOfTasks):
                print("The List of Tasks is Empty, WoHoo!\n")
                continue
            else:
                print("The List of Incomplete Tasks:")
                i = 1
                for task in theSetOfTasks:
                    print(f"{str(i)}. {task} - incomplete")
                    i += 1
                selection = int(input("Enter the task number: "))
                print(f"Task '{theSetOfTasks[selection - 1]}' was marked as completed and removed from the list of tasks.\nCongrats! (:\n")
                theSetOfTasks.remove(theSetOfTasks[selection - 1])
                
        # 3. view all tasks
        elif val == 3:
            if IsListEmpty(theSetOfTasks):
                print("The List of Tasks is Empty, WoHoo!\n")
                continue
            print("The List of Tasks:")
            i = 1
            for task in theSetOfTasks:
                print(f"{str(i)}. {task}")
                i += 1

        # 4. quit
        elif val == 4:
            break
        
        # exceptions
        else:
            print("Invalid Input! Give a valid input (1 - 4).\n")
            continue
except:
    print("\n\n\t\tWhy Must you Torture Me In This Way.\n")
    print("An exception occured! \n(probably a type miss match in some input statement)")