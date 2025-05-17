

n= int (input("Enter a number: "))
for i in range(1,11):
	print( f"{n} * {i} = {n*i}")


'''
#its also possible to use the while loop
n= int (input("Enter a number: "))
i=1
while i<=11:    
    print( f"{n} * {i} = {n*i}")
    i=+1

'''


#Revers or multiplication table
n= int (input("Enter a number: "))
for i in range(1,11):
    print( f"{n} * {11-i} = {n * (11-i)}")
