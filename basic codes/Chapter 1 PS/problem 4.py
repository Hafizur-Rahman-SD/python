
# Problem 5 is included with this code comment 


import os

# Get current working directory
path = os.getcwd()

# List all files and folders in the current directory
contents = os.listdir(path)

print("Contents of the current directory:")
for item in contents:
    print(item)
