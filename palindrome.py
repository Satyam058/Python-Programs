def ispallindrom(s):
    s=s.lower()
    n=len(s)
    l=0
    h=n-1
    r=1
    while l<=h:
      
        if s[l]==s[h]:
            l+=1
            h-=1
            continue
        
        if s[l].isalnum() and s[h].isalnum():
            r=0
            return r
        
        elif s[l].isalnum():
            h-=1
        else:
            l+=1
    return r
s="A man, a plan, a canal: Panama"
print("%d" %ispallindrom(s))
