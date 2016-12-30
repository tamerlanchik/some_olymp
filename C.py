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
def dfc(i, j):
    #print("Hello: ", i, j)
    if i==j:
        #print("Reached")
        return 0
    ls=[]
    for p in range(1, n+1):
        #print(i, p)
        if F[i][p]==1:
            #print(visited)
            if visited[p]==0:
                
                #print(i, p)
                #print(visited)
                visited[p]=-2
                ans=dfc(p, j)
                if ans!=-1:
                    ls.append(ans+1)
                    #print("Ls-app: ", ls, ans+1)
                visited[p]=0
            '''else:
                if visited[p]>0:
                    if len(ls)>0:
                        ls[-1]=min(ls[-1], visited[i][p]+1)
                    else: ls.append(visited[i][p]+1)
                    visited[i][p]=ls[-1]
                    print("New road", i, p, j, ls[-1])'''
    else:
        if len(ls)>0:
            return min(ls)
        else:
            #print("Break way", (i, j))
            return -1
Ans=float("inf")
for i in pars:
    l=0    
    lens.append(0)
    visited=[0]*(n+1)
    visited[i[0]]=-2
    #print("Start: ", i)
    z=dfc(i[0], i[1])
    if z>0:
        Ans=min(z, Ans)
    #print("Finish: ", Ans)
    #if lens[-1]==0: lens.pop()
#print(min(lens))
#print(lens)
print(Ans)
        
            
        
