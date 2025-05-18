#1. Write a program using functions to find greatest of three numbers. 


def find_greatest_number(num1, num2, num3):
    """
    Function to find the greatest of three numbers.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
num3 = float(input("Enter third number: "))
# Call the function and print the result
greatest_number = find_greatest_number(num1, num2, num3)
print(f"The greatest number  is: {greatest_number}")