def factorial(a):
    i=1
    fac=1
    while i<=a:
        fac=fac*i
        i+=1
    return fac
b=int(input())
print(factorial(b))