tasks_list= []

def add_task():
    task=input("Enter your task: ")
    tasks_list.append(task)
    print("Task added")

def view_task():
    a=len(tasks_list)
    s=1
    i=0
    while(s<=a):
        print(s,".",tasks_list[i])
        i=i+1
        s=s+1

def delete_task():
    view_task()
    task_no=int(input("Enter the no. of the task to delete: "))-1

    if task_no>=0 and task_no<len(tasks_list):
        del tasks_list[task_no]
        print("Task deledted.")
    else:
        print("Invalid task number")
        

while True:
    print("Menu:")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")
    user_choice=input("Enter your choice(1-4): ")



    if user_choice=="1":
        add_task()
    elif user_choice=='2':
        view_task()
    elif user_choice=='3':
        delete_task()
    elif user_choice=='4':
        print("Goodbye!!")
        break
    else:
        print("Enter valid input")
