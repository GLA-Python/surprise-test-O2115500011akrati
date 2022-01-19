def fun_exp(l):
    data=[]
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            a=l[i]-l[i+1]
        else:
            a=l[i+1]-l[i]
        data.append(a)
    print(data)

#data list sorting
    c = 0
    j = 0
    while j < len(data)-1:
        if(data[j] > data[j + 1]) or (data[j]==data[j+1]):
            c = 1
        j += 1
        
        
    return False if c==1 else True

    
lst=list(map(int,input().split()))
print(lst)
print(fun_exp(lst))

