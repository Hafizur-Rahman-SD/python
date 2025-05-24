# #1. Write a program to read the text from a given file ‘poemfile.txt’ and find out  whether it contains the word ‘shimmer’


f =open ("poem_file.txt")

content = f.read()

if ("shimmer"in content ):
    print("The Word is present in the content")

else:
    print("The word is not exist in here")


    f.close()