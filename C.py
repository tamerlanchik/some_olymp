import queue
n, m=map(int, input().split())
a=list(map(int, input().split()))

pars=[]
for i in range(n):
    for j in range(i+1, n): 
        if a[i]*a[j]!=0 and a[i]!= a[j]:
            pars.append((i, j))
del a            
F=[[] for i in range(n)]
for i in range(m):
    x, y=map(int, input().split())
    F[x-1].append(y-1)
    F[y-1].append(x-1)

dist=[[-1]*n for i in range(n)]
for i in range(n):
    dist[i][i]=0
for k in pars:
    i=k[0]
    q=queue.Queue()
    q.put(i)
    while not q.empty():
        u=q.get()
        for v in F[u]:
            if dist[i][v]==-1:
                dist[i][v]=dist[i][u]+1
                q.put(v)
ans=float("inf")
for i in pars:
    a=dist[i[0]][i[1]]
    if a>0:
        ans=min(ans, a)
print(ans)

