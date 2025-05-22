
# #from 1 file theyer multiple line in a file i want to read a particula line from my file and shows the data. 

f=open("readfile.txt") #file open for read data 

lines = f.readline() #function call for read all data line by line but in output we can see the first line of our files 
print(lines,type(lines))  # print the file with tyer type cast 

line1 =f.readline()  # for see a particular line in file and print this
print(line1)

line2 =f.readline()
print(line2)

line3 =f.readline()
print(line3)


line7 =f.readline()
print(line7)

f.close()  # must close  



#we can do this same work in simple code here it 
#shortcut but good way to write programm 

# f = open("readfile.txt")  # open the file before reading
# line = f.readline()
# while (line != ""):
#     print(line)
#     line = f.readline()
# f.close()