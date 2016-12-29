a, b, c = map(int, input().split())
n=int(input())
F=[0]*(n+1)
for i in range(1, n+1):
    x=F[max(0, i-28)]
    y=F[max(0, i-7)]
    z=F[i-1]
    F[i]=min(x+c, y+b, z+a)
print(F[-1])
