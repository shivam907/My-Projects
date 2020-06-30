t = int(input())
l=[]
for i in range(0,t):
    l=list(map(int, input().split()))
    s=l[0]
    n=l[1]
    c=0
    while s>1:
        
        for i in range(n, 1, -2):
            # if s%i==0 and s!=0:
            #     c+=1
            #     s=s-i
            if s>=i:
                c=c+s//i
                s=s-((s//i) * i)
                
    if s!=0:
        c=c+s
    l.append(c)
for i in l:
    print(i)

