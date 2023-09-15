def maxof_3(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
e=int(input())
f=int(input())
g=int(input())
d=maxof_3(e,f,g)
print(d)