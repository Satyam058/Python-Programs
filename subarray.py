class subarr:
    arr=[2, 1, -3, 4, -1, 2, 1, -5, 4]
    i=0
    sum=0
    max=0
    h=[]
    while i<len(arr):
        k=i
        while k<len(arr):
            sum=sum+arr[k]
            h=h+[arr[k]]
            
            if(sum>=max):
                max=sum
                a=h
                h=[]
            k+=1
                
        h=[]
        i+=1
        sum=0
    print(a)
    print(max)
    
            
