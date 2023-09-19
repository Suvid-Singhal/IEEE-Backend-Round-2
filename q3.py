class gen_subsets:
    inp=eval(input("Enter the list: "))
    import itertools
    ans=[[]]
    for i in range(1,len(inp)+1):
        f=list(itertools.combinations(inp,i))
        for j in range(len(f)):
            f[j]=list(f[j])
        ans.extend(f)
    

subsets=gen_subsets()
print(subsets.ans)
