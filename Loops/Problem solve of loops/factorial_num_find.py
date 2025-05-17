# Program to find the factorial of a number using a loop
# 5! = 1 X 2 X 3 X 4 X 5
# 5! = 120

n= int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
   fact= fact*i

   print(f"The factorial of {n} is {fact}")