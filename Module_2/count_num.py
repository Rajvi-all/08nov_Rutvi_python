Name=input("enter your full name:")

for i in Name:
    frequency = Name.count(i)
    print(str(i) + ":" + str (frequency), end=",")
