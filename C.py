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

lens=[]
visited=[0]*(n+1)
distanses=[[-1]*(n+1) for i in range(n+1)]
for k in range(n+1):
    distanses[k][k]=0
def dfc(i, j):
    if distanses[i][j]>=0:
        return distanses[i][j]
    ls=[]
    for p in range(1, n+1):
        if F[i][p]==1:
            distanses[i][p]=distanses[p][i]=1
            if visited[p]==0:
                visited[p]=-2
                ans=dfc(p, j)
                if ans>=0:
                    ls.append(ans+1)
                    if distanses[i][j]>=0:
                        t=min(ans, distanses[i][j])
                    else:
                        t=ans
                    distanses[i][j]=distanses[j][i]=t+1
                visited[p]=0
    else:
        if len(ls)>0:
            q=min(ls)
            distanses[i][j]=distanses[j][i]=q
            return q
        else:
            return -2
Ans=float("inf")
for w in pars:
    l=0    
    lens.append(0)
    visited=[0]*(n+1)
    visited[w[0]]=-2
    z=dfc(w[0], w[1])
    if z>0:
        Ans=min(z, Ans)
print(Ans)
