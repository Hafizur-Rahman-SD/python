#4. Write a program to find whether a given number is prime or not. 
# A prime number is a number that is only divisible by 1 and itself.

n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break   #if the number is divisible by any number other than 1 and itself, it is not prime
else:
    print(f"{n} is a prime number")
