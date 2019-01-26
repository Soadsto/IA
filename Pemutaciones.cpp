#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int NMAX, cont = 0;
bool finished = false;

void procesar_solucion(vector<int> a, int k)
{
	cont++;
	for(int i = 0; i < k; i++)
		printf(" %d", a[i]);
	cout << endl;
}

bool es_solucion(vector<int> a, int k, int n)
{
	return k == n;
}

void construct_candidates(vector<int> a, int k, int n, vector<int> &c, int &cand)
{
	vector<bool> en_perm(NMAX);
	int i;
	for(i = 0; i < NMAX; i++)
		en_perm[i] = false;
	for(i = 0; i < k; i++)
		en_perm[a[i] - 1] = true;
	cand = 0;
	for(i = 1; i <= n; i++)
		if(!en_perm[i - 1])
			c[cand++] = i;
}

void backtrack(vector<int> &a, int k, int n)
{
	vector<int> c(NMAX);
	int ncandidates;
	if(es_solucion(a, k, n))
		procesar_solucion(a, k);
	else
	{
		construct_candidates(a, k++, n, c, ncandidates);
		for(int i = 0; i < ncandidates; i++)
		{
			a[k - 1] = c[i];
			backtrack(a, k, n);
			if(finished)
				return;
		}
	}
}

void permutaciones(int n)
{
	vector<int> a(NMAX);
	backtrack(a, 0, n);
}

void prueba(vector<int> &a)
{
	a.push_back(10);
}

int main()
{
    int n;
	cin >> n;
	NMAX = n;
	permutaciones(n);
	cout << "\n\nSoluciones: " << cont << endl;
	return 0;
}
