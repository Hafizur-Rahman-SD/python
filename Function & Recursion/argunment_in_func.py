



def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "smile"

a= goodDay("Hafizur", "    Thank you") 

print(a)



#defult arguments

def goodDay(name, ending="Have a Good day"):
    print(f"Good Day, " + name)
    print(ending)

goodDay("Hafizur","Thanks") # default argument
goodDay("Rahman") # default argument