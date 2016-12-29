k=int(input())
l=input()
s=[i+1 for i in range(len(l)) if l[i]=='1']
L=len(s)
for i in range(len(s)-1):
    a=s[min(i+k, L-1)]-s[i]
    print(a*2, end=' ')
print(0)
