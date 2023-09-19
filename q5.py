t=int(input())
while t>0:
    n=int(input())
    lst=input().split()
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    one=lst[::2]
    two=[]
    try:
        two=lst[1::2]
    except:
        pass
    for i in range(len(one)):
        one[i]=abs(one[i])
    for i in range(len(two)):
        two[i]=abs(two[i])
    one.sort()
    two.sort(reverse=True)
    try:
        one[0],two[0]=two[0],one[0]
    except:
        pass 
    print(sum(one)-sum(two))
    t-=1
