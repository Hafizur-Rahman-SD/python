
#how to take input from user.int must use beacuse without it it will take string input.
a= int (input("Enter your age number: "))

if (a>18):   # If statenment 
	print ("You are eligible to vote")
	print ("Its Good for your Country")
    

elif(a==0):
    print("You are entering 0 which is not a valid age") 

elif (a<0):
	print ("You are enter an invalide age -number not your age ")
else:   
	print ("You are not eligible for vote")
# The above code checks if a person is eligible to vote based on their age.

  
