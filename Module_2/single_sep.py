name=input('enter your name:')
sr=input('enter your surname:')

#get single string_________________________

print(name,end=" ")
print(sr)

#swap first two character of each sring____________

r = sr[:2] + name[2:]
N = name[:2] + sr[2:]

print(r)
print(N)