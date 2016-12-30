//============================================================================
// Name        : sdf.cpp
#include <iostream>
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
	int counter=0;
	for (int i=1; i<=n; i++)
	{
		x=F[max(0, i-28)-counter];
		y=F[max(0, i-7)-counter];
		z=F[i-1-counter];
		F[i-counter]=mini(x+c, y+b, z+a);
		if (i-counter>28)
		{
            F+=1;
            counter+=1;
		}
    }
    cout<<"Ans: "<<F[n-counter]<<endl;
	return 0;
}
