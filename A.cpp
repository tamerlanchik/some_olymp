//============================================================================
// Name        : sdf.cpp
#include <iostream>
#include <algorithm>
using namespace std;

inline int mini(int a, int b, int c)
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
	int a, b, c, x, y, z;
	int n;
	cin>>a>>b>>c;
	cin>>n;
	int *F=new int [n+1];
	F[0] = 0;
	for (int i=1; i<=n; i++)
	{
		x=F[max(0, i-28)];
		y=F[max(0, i-7)];
		z=F[i-1];
		F[i]=mini(x+c, y+b, z+a);
    }
    cout<<F[n];
	return 0;
}
