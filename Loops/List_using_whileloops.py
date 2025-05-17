# Here we see how to use while loops to create a list of numbers


l=[ 1,2,17,"Hafiz", "rahman", "Rony", "Harry", "Hamid", "Hassan", "True"]

i=0
while (i < len(l)):
    # This is the body of the loop, which will be executed as long as the condition is true
    print(l[i])
    i += 1
