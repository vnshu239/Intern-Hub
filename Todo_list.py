def Todo():
    print("Welcome to Todo App \n")
    Tasks = []

    while True:
        print("------------------------------")
        choice = int(input("Enter your Choice \n 1. Add Task \n 2. Update Task \n 3. Delete Task \n 4. View All Task \n 5. Exit App \n"))
        print("------------------------------")

        if(choice == 1):
            task = input("Enter your task: ")
            Tasks.append(task)
            print(f"Task {task} added successfully!!")
        elif(choice == 2):
            ut = input("Which Task You Want to Delete : ")
            ind = Tasks.index(ut)
            ntask = input("Enter Updated Task : ")
            Tasks[ind] = ntask
            print(f"Task {ntask} Updated Successfully!!")
        elif(choice == 3):
            ut = input("Which Task You Want to Delete : ")
            ind = Tasks.index(ut)
            del Tasks[ind]
            print(f"Task {ut} Deleted Successfully!!")
        elif(choice == 4):
            i = 1
            if(len(Tasks) < 1):
                print("No Tasks Available!!")
            else :
                for task in Tasks:
                    print(f"{i}.{task}\n")
                    i += 1
                print("All Task Displayed Successfully!!")
        else:
            print("Exiting App!!")
            break

Todo()