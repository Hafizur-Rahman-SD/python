 

a= "This is an Global Variable"   # Define what type of var of this for 1 number output.

def f(): # create a function 


    global a # call the global var. 
    a = "We Fixed this variable globally"  #Again store some value in Var so first var value is nothing. 
    # again if we comment this linevthen our output will come first value.
    
    print(a)  # print this value foe 1st time.

f() # Again call the function for pirint 2nd time .
print(a)   #PRINnt the valu for 2nd time 