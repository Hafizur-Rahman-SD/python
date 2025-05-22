# Here is a program that we want to read a file by our program. i have hafizur.txt file

f = open("hafizur.txt")  #Call a function for open my file
data = f.read()          #Call function to read my file 
print (data)             # Print the data what in my file 
f.close()                # colse the file when it compleate in read data (its important for good practice)