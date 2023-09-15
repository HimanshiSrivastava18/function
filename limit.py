def limit(u,l,n):
    if n>=l and n<=u:
        return True
    else:
        return False
a=int(input())
b=int(input())
c=int(input())
d=limit(a,b,c)
print(d)