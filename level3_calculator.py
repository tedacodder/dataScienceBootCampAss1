history=[]

def add(x,y):
    res=x+y
    history.append(f"{x} + {y} = {res}")
    return res

def subtract(x,y):
    res= x-y
    history.append(f"{x} - {y} = {res}")
    return res

def multiply(x,y):
    res=x*y
    history.append(f"{x} * {y} = {res}")
    return res

def divide(x,y):
    if y==0:
        return "Error: Division by zero"
    res=x/y
    history.append(f"{x} / {y} = {res}")
    return res

def calculator():
    #CLI-Based calculator.

    while True:
        print("\n----Calculator----")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        print("6.show history")
        choice=input("Choose an operation (1-6): ")
        if choice=="5":
            print("Exiting calculator ...")
            break

        elif choice=="6":
            print("\n---History---")
            for i in history:
                print(i)
            continue
        #Input numbers
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))

        #perform operation
        if choice=="1":
            print("Result: ",add(num1,num2))
        elif choice=="2":
            print("Result: ",subtract(num1,num2))
        elif choice=="3":
            print("Result: ",multiply(num1,num2))
        elif choice=="4":
            print("Result: ",divide(num1,num2))
        elif choice=="6":
            print("\n---History---")
            for i in history:
                print(i)
        else:
            print("Invalid choice. Try again.")
            
                 
#run the program
calculator()
