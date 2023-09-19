s1=input("Enter s1: ")
s2=input("Enter s2: ")
chars={}
for i in s1:
    if i in chars:
        chars[i]+=1
    else:
        chars[i]=1
res=1
for i in chars:
    cnt=0
    for j in s2:
        if j==i:
            cnt+=1
    if cnt<chars[i]:
        res=0
        break
if res==1:
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")
