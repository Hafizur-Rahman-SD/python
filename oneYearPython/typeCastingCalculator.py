

# x="10"
# y =int(x)  # Type casting from string to integer
# print(y+5)  # Output: 15 

# A= "3.14"
# B =(float(A))  # Type casting from string to float
# print(B + 1.86)  # Output: 5.0

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator!")
