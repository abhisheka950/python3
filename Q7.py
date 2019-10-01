N=range(0,1000)
a=[]
for i in N:
    s=0
    a=list(str(i))
    for j in a: 
        s=s+(pow(int(j),3))
    if s==i:
        print(s)
    
