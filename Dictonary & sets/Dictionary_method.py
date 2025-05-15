
# d={}    This is a empty dictionary.

marks ={
"Hafizur": 100,
"Rahman": 90,       
"Shakib": 95,
"Riyad": 85,
"Asma": 80,
}

print(marks. items()) # it will give us all the items in the dictionary


print(marks.keys()) # it will give us all the keys in the dictionary
print(marks.values()) # it will give us all the values in the dictionary

marks.update ({"Abdullah": 70, "Sakti": 50}) # it will add a new key value pair in the dictionary
print(marks) # it will give us all the items in the dictionary

print(marks.get("liza")) # it will give us the value of the key Hafizur

popitem = marks.popitem() # it will remove the last item from the dictionary
print(popitem) # it will give us the last item in the dictionary

print(marks) # it will give us all the items in the dictionary
print(marks.pop("Hafizur")) # it will remove the key Hafizur from the dictionary