//============================================================================
// Name        : sdf.cpp
#include <iostream>
using namespace std;

inline int mini(unsigned long long a, unsigned long long b, unsigned long long c)
{
	if (a>b)
	{
		if (b<c) return b;
		else return c;
	}
	else{
		if (a<c) return a;
		else return c;
	}
}
int main() {
	unsigned long long a, b, c, x, y, z;
	unsigned long long n;
	cin>>a>>b>>c;
	cin>>n;
	unsigned long long *F=new unsigned long long [n+1];
	F[0] = 0;
	for (unsigned long long i=1; i<=n; i++)
	{
		x=F[max((unsigned long long)0, i-28)];
		y=F[max((unsigned long long)0, i-7)];
		z=F[i-1];
		F[i]=mini(x+c, y+b, z+a);
    }
    cout<<F[n];
	return 0;
}
