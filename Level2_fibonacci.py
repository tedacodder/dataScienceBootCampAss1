def generate(n):
    #Generate a Fibonacci sequence of n numbers.
    if n<=0:
        return []
    sequence=[0]#the first number
    if n==1:
        return sequence
    sequence.append(1)#the second number

    #let generate the remaining numbers
    for i in range(2,n):
        nextNum=sequence[-1]+sequence[-2]
        sequence.append(nextNum)

    return sequence

#input from user

num=int(input("Enter the number of the term for fibonacci seq: "))
print("Fibonacci sequence: ")
print(generate(num))
    
    
    
