print("----------------------------------------Welcome----------------------------------------")

ch = input("Do you want to \n 1.choose your options \n 2.enter your expression manually\n")

match ch:
    case '1':
        num1=input("enter first Number:")
        num2=input("enter second Number:")
        choice=input("enter your choice of operator:\n1.+\n2.-\n3.x\n4./\n")
        match choice:
            case '1':
                print(num1+num2)
            case '2':
                print(num1-num2)
            case '3':
                print(num1*num2)
            case '4':
                print(num1/num2)
    case '2':
        exp=input("enter your experssion:")
        print(eval(exp))