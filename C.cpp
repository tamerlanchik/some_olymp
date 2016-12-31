#include <iostream>
#include <vector>
#include <queue>
int main()
{
	unsigned int n, m;
	std::cin >> n >> m;
	unsigned int *a = new unsigned int[n];
	for (auto i = 0; i < n; i++)
		std::cin >> a[i];

	std::vector<unsigned int>pars;
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
	unsigned int x, y;
	std::vector<unsigned int> *F = new std::vector<unsigned int>[n];
	for (auto i = 0; i < m; i++)
	{
		std::cin >> x >> y;
		F[x - 1].push_back(y - 1);
		F[y - 1].push_back(x - 1);
	}


	unsigned int *i=new unsigned int;
	unsigned int u;
	unsigned int ans = 1000000000;
	unsigned int aw;
	unsigned int *dist = new unsigned int[n];
	std::queue<unsigned int> *q = new std::queue<unsigned int>;
	for (auto k = 0; k < pars.size(); k += 2)
	{
		*i = pars[k];
		
		q->push(*i);
		for (auto l = 0; l < n; l++)
			dist[l] = -1;
		dist[*i] = 0;
		while (!q->empty())
		{
			u = q->front(); q->pop();
			for (auto v:F[u])
				if (dist[v] == -1)
				{
					dist[v] = dist[u] + 1;
					q->push(v);
				}
		}
		aw = dist[pars[k + 1]];
		if (aw > 0) ans = std::min(ans, aw);
	}

	std::cout << ans;
	return 0;
}
