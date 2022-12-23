a=11
b=12

#with temp var
temp=a 
a=b
b=temp
print("the value after swap a=",a)
print("the value after swap b=",b)

#without temp
a,b=b,a
print("the value after swap a=",a)
print("the value after swap b=",b)
