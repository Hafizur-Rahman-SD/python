'''

    3 problem in i 1 file. 
7. Write a program to print the following star pattern. 
* 
*** 
***** for n = 3 
8. Write a program to print the following star pattern: 
* 
** 
***      for n = 3 
9. Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * * 
'''
n= int(input("Enter a number: "))
for i in range(1,n+1):
    print (" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")



'''8. Write a program to print the following star pattern:     
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print("*"* i, end="")
    print("")
''' 

'''9. Write a program to print the following star pattern.
    n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")

    '''