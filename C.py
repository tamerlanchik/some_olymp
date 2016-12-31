import queue
n, m=map(int, input().split())
a=list(map(int, input().split()))
F=[[0]*(n) for i in range(n)]
for i in range(m):
    x, y=map(int, input().split())
    F[x-1][y-1]=1
    F[y-1][x-1]=1
pars=[]
for i in range(n):
    for j in range(i+1, n): 
        if a[i]*a[j]!=0 and a[i]!= a[j]:
            pars.append((i, j))

dist=[[-1]*n for i in range(n)]
for i in range(n):
    dist[i][i]=0
for k in pars:
    i=k[0]
    q=queue.Queue()
    q.put(i)
    while not q.empty():
        u=q.get()
        for v in range(n):
            if F[u][v]==1 and dist[i][v]==-1:
                dist[i][v]=dist[i][u]+1
                q.put(v)
ans=float("inf")
for i in pars:
    a=dist[i[0]][i[1]]
    if a>0:
        ans=min(ans, a)
print(ans)

