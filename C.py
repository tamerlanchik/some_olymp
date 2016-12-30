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
#print("pars: ", pars)
#for i in F:
#    print(*i)
lens=[]
visited=[0]*(n+1)
distanses=[[-1]*(n+1) for i in range(n+1)]
for k in range(n+1):
    distanses[k][k]=0
def dfc(i, j):
    print("Hello: ", i, j)
    if distanses[i][j]>=0:
        print("Reached")
        return distanses[i][j]
    if i==j:
        print("Reached")
        return 0
    ls=[]
    for p in range(1, n+1):
        print(i, p)
        if F[i][p]==1:
            print(visited)
            if visited[p]==0:
                
                print(i, p)
                print(visited)
                visited[p]=-2
                ans=dfc(p, j)
                if ans>=0:
                    ls.append(ans+1)
                    print("New road: ", ls)
                    if distanses[i][p]>=0:
                        t=min(ans, distanses[i][p])
                    else:
                        t=ans
                    distanses[i][p]=distanses[p][i]=t+1
                visited[p]=0
    else:
        if len(ls)>0:
            q=min(ls)
            distanses[i][j]=distanses[j][i]=q
            print("Renew data: ", q, i, j)
            for i in distanses:
                for j in i:
                    if j>=0:
                        print('', j, end='')
                    else:
                        print(j, end='')
                print()            
            return q
        else:
            print("Break way", (i, j))
            return -2
Ans=float("inf")
for w in pars:
    l=0    
    lens.append(0)
    visited=[0]*(n+1)
    visited[w[0]]=-2
    print("Start: ", w)
    z=dfc(w[0], w[1])
    if z>0:
        Ans=min(z, Ans)
    print("Finish: ", w, z)
    #if lens[-1]==0: lens.pop()
#print(min(lens))
#print(lens)
print(Ans)
for i in distanses:
    for j in i:
        if j>=0:
            print('', j, end='')
        else:
            print(j, end='')
    print()

'''
9 8
5 1 7 0 2 0 0 1 5
1 9
1 7
2 7
2 6
2 4
3 4
4 5
6 7
'''
