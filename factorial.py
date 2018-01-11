#Program to find factorial of a number
n=int(input('Enter a value:\n'))

fact=1
Factorial=[]
if n<0:
    print("Sorry, no factorial for negative number.\n")

elif n==0:
    print("Factorial is 1.\n")

else:
    for i in range(1,n+1):
         fact=fact*i
         Factorial.append(fact)
    print("Factorial of",n,"is",fact,"\n")
    print("The list of factorial of all numbers from 1 upto the given number:\n",Factorial)
