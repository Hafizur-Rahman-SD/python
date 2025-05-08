# Function input.py
# This program demonstrates the use of eval() function
# eval() can be dangerous if you're taking input from an untrusted user. It runs the input as Python code.
# problem is :3. Check the type of variable assigned using input () function.






a = eval(input("Enter something: "))
print("Type of a is:", type(a))
