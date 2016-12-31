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

	unsigned int u;
	unsigned int ans = 1000000000;
	unsigned int aw;
	unsigned int *dist = new unsigned int[n];
	std::vector<unsigned int> *F = new std::vector<unsigned int>[n];
	unsigned int x, y;
	for (auto i = 0; i < m; i++)
	{
		std::cin >> x >> y;
		F[x - 1].push_back(y - 1);
		F[y - 1].push_back(x - 1);
	}
	std::queue<unsigned int> q;
	for (auto i = 0; i < n; i++)
	{
		for (auto j = i + 1; j < n; j++)
			if ((a[i] * a[j] != 0) && (a[i] != a[j]))
			{
				q.push(i);
				for (auto l = 0; l < n; l++)
					dist[l] = -1;
				dist[i] = 0;
				while (!q.empty())
				{
					u = q.front(); q.pop();
					for (auto v : F[u])
						if (dist[v] == -1)
						{
							dist[v] = dist[u] + 1;
							q.push(v);
						}
				}
				aw = dist[j];
				if (aw > 0 && aw < ans) ans = aw;
			}
	}

	std::cout << ans;
	return 0;
}
