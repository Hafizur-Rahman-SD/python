
'''4. A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file. '''


word = "Donkey"

with open("4_change_file_content.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("4_change_file_content.txt", "w") as f:
    f.write(contentNew)