name = input('enter your name:')

if (len(name)%4==0):
    print(name[::-1])
else:
    print("cant't")
    