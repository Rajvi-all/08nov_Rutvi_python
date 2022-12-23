mystr = input('enter any sentence:')

a=0
for i in mystr:
    a=a+1
newstr=mystr[0:2]+mystr[a -2:a]

print(mystr)
print(newstr)