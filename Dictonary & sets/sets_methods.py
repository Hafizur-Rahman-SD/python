

## Set methods
# Set is a collection of unordered and unindexed elements

s = {1, 5, 32, 54,5, 5, 5, "Hafizur"}

print(s, type(s))

s.add(777)  # add a new element to the set
print(s, type(s)) #type(s) will give us the type of the set
s.remove(1)  # remove an element from the set
print(s, type(s))



#another code for union 

s1 = {1, 75, 7, 78,13,8,54}  
s2 = {7, 8, 1, 78,43,50,89,445,3,2,1}

print(s1.union(s2))   # it will give us the union of two sets


print(s1.intersection(s2)) # it will give us the intersection of two sets