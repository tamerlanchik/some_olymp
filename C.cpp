#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int main()
{
	unsigned int n, m;
	unsigned int x, y;
	cin >> n >> m;
	//vector <unsigned int> *a=new vector<unsigned int>;
	//a->resize(n);
	unsigned int *a = new unsigned int[n];
	for (auto i = 0; i < n; i++)
		cin >> a[i];

	vector<unsigned int>pars;
	for (auto i = 0; i < n; i++)
	{
		for (auto j = i + 1; j < n; j++)
			if ((a[i] * a[j] != 0) && (a[i] != a[j]))
			{
				pars.push_back(i);
				pars.push_back(j);
			}
	}
	delete[] a;
	vector<vector<bool>> F(n, vector<bool>(n, 0));
	for (auto i = 0; i < m; i++)
	{
		cin >> x >> y;
		F[x - 1][y - 1] = true;
		F[y - 1][x - 1] = true;
	}
	vector<vector<unsigned int>> dist(n, vector<unsigned int>(n, -1));
	for (auto i = 0; i < n; i++)
		dist[i][i] = 0;
	unsigned int i;
	for (auto k = 0; k < pars.size(); k += 2)
	{
		i = pars[k];
		queue<unsigned int> q;
		q.push(i);
		while (!q.empty())
		{
			unsigned int u = q.front(); q.pop();
			for (unsigned int v = 0; v < n; v++)
				if (F[u][v] == true && dist[i][v] == -1)
				{
					dist[i][v] = dist[i][u] + 1;
					q.push(v);
				}
		}
	}
	unsigned int ans = 1000000000;
	unsigned int aw;
	for (auto i = 0; i < pars.size(); i+=2)
	{
		aw = dist[pars[i]][pars[i + 1]];
		if (a > 0) ans = min(ans, aw);
	}
	cout << ans;
	cin >> n;
	return 0;
}
