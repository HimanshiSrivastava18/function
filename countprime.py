def prime (num):
    j=2
    count=0
    while j<=num:
        if num%j==0:
            count+=1
        j+=1
    if count==1:
        return True
    else:
        return False
i=2
count=0
n=int(input("Enter a number: "))
while count<n:
    if prime(i):
        count+=1
        a=i
    i+=1
print(a)
    