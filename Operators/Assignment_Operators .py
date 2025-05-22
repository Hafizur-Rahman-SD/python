
#Traditional way to write code 
# a = 10
# b = a
# print(b)
# b += a
# print(b)
# b -= a
# print(b)
# b *= a
# print(b)
# b <<= a
# print(b)




# Taking input from the user
a = int(input("Enter the value of a: "))

# Assigning a to b
b = a
print("Initially, b =", b)

# Adding a to b
b += a
print("After b += a, b =", b)

# Subtracting a from b
b -= a
print("After b -= a, b =", b)

# Multiplying b by a
b *= a
print("After b *= a, b =", b)

# Left shifting b by a bits
b <<= a
print("After b <<= a, b =", b)

