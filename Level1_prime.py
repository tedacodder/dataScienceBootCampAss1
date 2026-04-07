def is_prime(num):
    #check if a number is prime

    #first we have to handle the edge cases
    if num<=1:
        return False
    
    """
    #the time complexity of this is O(n) but we can do better
    #check the divisiblity up to n-1
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True
"""
    #we only have to check up to rad(n) which will have the time complexity of O(n**0.5)
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
#we take input
number=int(input("Enter a number : "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
