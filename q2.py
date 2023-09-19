n=int(input("Enter n: "))
board=[]
for i in range(n):
    board.append([0]*n)
row=0
col=0
bounds=n-1
sizeleft=n-1
check=1
mov='r'
for i in range(1,n*n+1):
    board[row][col]=i
    if mov=='r':
        col+=1
    elif mov=='l':
        col-=1
    elif mov=='u':
        row-=1
    elif mov=='d':
        row+=1
    if i==bounds:
        bounds+=sizeleft
        if check!=2:
            check=2
        else:
            check=1
            sizeleft-=1
        if mov=='r':
            mov='d'
        elif mov=='d':
            mov='l'
        elif mov=='l':
            mov='u'
        elif mov=='u':
            mov='r'
for i in range(n):
    for j in range(n):
        print(f'{board[i][j]:4}',end="")
    print()
