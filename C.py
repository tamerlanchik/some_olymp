
n, m=map(int, input().split())
a=[0]+list(map(int, input().split()))
F=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    x, y=map(int, input().split())
    F[x][y]=1
    F[y][x]=1

pars=[]
for i in range(1, n+1):
    for j in range(i, n+1):
        if a[i]*a[j]!=0 and a[i]!= a[j]: pars.append((i, j))
print("pars: ", pars)
for i in F:
    print(*i)
lens=[]
visited=[[0]*(n+1) for j in range(n+1)]
def dfc(i, j):
    print("Hello: ", i, j)
    if i==j:
        print("Reached")
        return 0
    ls=[]
    for p in range(1, n+1):
        print(p)
        if F[i][p]==1:
            if visited[i][p]==0:
                visited[i][p]=visited[p][i]=-2
                #print(i, p)
                for l in visited:
                    print(*l)
                ans=dfc(p, j)
                if ans!=-1:
                    visited[i][p]=visited[p][i]=ans+1
                    ls.append(ans+1)
                    print("Ls-app: ", ls, ans+1)
                else:
                    visited[i][p]=visited[p][i]=-1
            else:
                if visited[i][p]>0:
                    print("Ls: ", ls)
                    ls[-1]=min(ls[-1], visited[i][p]+1)
                    visited[i][p]=ls[-1]
    else:
        if len(ls)>0:
            return min(ls)
        else:
            print("Break way", (i, j))
            return -1
for i in pars:
    l=0    
    lens.append(0)
    visited=[[0]*(n+1) for j in range(n+1)]
    print("Start: ", i)
    Ans=dfc(i[0], i[1])
    print("Finish: ", Ans)
    #if lens[-1]==0: lens.pop()
print(min(lens))
print(lens)

        
            
           
