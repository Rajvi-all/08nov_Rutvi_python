def fibo (n):
    if n==1 or n==0:
        return 1
    else:
        return fibo (n-1) + (n-2)

n=int(input("enter no:"))
for i in range (n):
    print(fibo(i),end=' ')