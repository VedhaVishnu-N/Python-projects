import os
filename=input("\nEnter your file name please:")+".txt"
def create_file():
    f=open(filename,'w')
    return "Your file has been created successfully"+filename

try:
    with open(filename,'r') as f:
        counter=len(f.readlines())+1
except:
    create_file()

def print_all():
    with open(filename) as f:
        for line in f:
            print(line)

def add_task(file,s):
    with open(file,'a')as f:
        f.write("\n"+str(s))
        
def delete_file():
    os.remove(filename)
    print("Your File has been deleted Successfully")

def print_task(task_no):
    with open(filename,'r') as f:
        for line in f:
            if line.startswith(str(task_no)):
                print(line)

def remove_task(task_no):
    tasks = []
    with open(filename, 'r') as f:
        tasks = f.readlines()

    with open(filename, 'w') as f:
        for task in tasks:
            if not task.startswith(str(task_no)):
                f.write(task)


print("--------------------------------WELCOME TO TODOLIST--------------------------------")
t=1
while t!=0:
    print("\nWhat Operation Do you want to Perform")
    ch=int(input("\n1.Create File \n2.Del File \n3.ADD Task \n4.Remove Task \n5.Print Certain Task \n6.Print All Tasks \n7.Exit\nOPTION:"))
    match ch:
        case 1:
            print(create_file())
        case 2:
            delete_file()
        case 3:
            s=str(counter)+'.'+input("Enter task you want to add:")
            add_task(filename,s)
            counter+=1
        case 4:
            pass
        case 5:
            task_no=int(input("Enter task No."))
            print_task(task_no)
        case 6:
            print_all()
        case 7:
            t=0
