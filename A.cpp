//============================================================================
// Name        : sdf.cpp
#include <iostream>
using namespace std;

inline int mini(unsigned long long int a, unsigned long long int b, unsigned long long int c)
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
	int **F=new int* [29];
	for(int i=0; i<=n; i++)
        F[i]=new int;
	*F[0] = 0;
	int counter=0;
	for (int i=1; i<=n; i++)
	{
        if (i>29)

		x=*F[max(0, i-28)];
		y=*F[max(0, i-7)];
		z=*F[i-1];
		*F[i]=mini(x+c, y+b, z+a);
		if (i-counter>29)
		{
            delete F[counter];
            counter+=1;
		}
    }
    cout<<*F[n];
    cout<<endl<<counter;
    cin>>x;
	return 0;
}
