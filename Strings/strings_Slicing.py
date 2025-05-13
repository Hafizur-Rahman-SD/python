# word = "amazing"
# word [1: 6: 2] # it will print the string from index 1 to index 6 with a step of 2

name = "Hafizur"

nameshort = name[0:3]                                   # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)                                   # it will print the character at index 1
character2 = name[2]
print(character2)                                   # it will print the character at index 2..........



# Slicing in python is a way to extract a portion of a string. It is done using the colon (:) operator within square brackets. The syntax for slicing is as follows:

name = "Hafizur"

print(name[0:2])

print(name[-3: -1])
print(name[1:6])

print(name[:6])                                   # is same as print(name[0:6])
print(name[1:])                                   # is same as print(name[1:7])
print(name[1:5])



# String functions
# 1. len() - Returns the length of the string.


name = "Hafizur"

print(len(name))
print(name.endswith("aur"))                    # Checks if the string ends with a specific substring.
print(name.find("i"))                          # Returns the index of the first occurrence of a substring in the string.
print(name.startswith("haf"))                  # Checks if the string starts with a specific substring.
print(name.capitalize())                       # Capitalizes the first letter of the string.
print(name.count("a"))                         # Counts the number of occurrences of a substring in the string.




a = 'Hafizur is a good boy\nbut not a bad \'boy\'' #how to use single and double quotes in a string. \n= new line


print(a)