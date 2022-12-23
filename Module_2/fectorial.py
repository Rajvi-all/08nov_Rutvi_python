"""def factorial (n):
    n=input("pls enter your no.")
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print=(factorial (n))"""
    
#======================

def fact (x):
    if x==0:
        return 1
    return x * fact(x - 1)
print(fact(5))    