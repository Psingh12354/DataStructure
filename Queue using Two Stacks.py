# Enter your code here. Read input from STDIN. Print output to STDOUT
new=[]
old=[]
for _ in range(int(input())):
    inp=list(map(int,input().split()))
    if inp[0]==1:
        new.append(inp[1])
    elif inp[0]==2:
        if len(old)==0:
            while new:
                old.append(new.pop())
        old.pop()
    else:
        print(old[-1] if old else new[0])
