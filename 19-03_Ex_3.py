task = []
option = 1
while option != '4':
    print(
"""Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program""")
    option = input()
    if option == '1':
        print("please insert the new task you want to do ")
        task.append(input())
    elif option == '2':
        print("which task you want to delete??")
        eliminare = input()
        task.remove(eliminare)
    elif option == '3':
        print(task)
quit()


