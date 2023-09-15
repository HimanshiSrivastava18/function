def  pangram(a):
    b="abcdefghijklmnopqrstuvwxyz"
    c=0
    i=0
    while i<len(b):
        if b[i] in a:
             c+=1
             i+=1
    if c==len(b):
        print("yes")
    else:
        print("not")
a="adgrtqwertuioplkjhgfdsazxcvbnm"
pangram(a)