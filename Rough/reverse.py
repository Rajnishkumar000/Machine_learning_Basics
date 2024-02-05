def rev(s,i):
    if i<1:
        return s[i]
    else:
        return s[i]+rev(s[:i],i-1)

k=input("Enter a String\n")
p=rev(k,len(k)-1)
print(p)