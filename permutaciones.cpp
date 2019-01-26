#include <iostream>
#include <vector>
using namespace std;
/*
    The art of Computer Programming PDF
    Knuth
    Addison-Wesley
    Vol I: Fundamental algorithms
    Vol II: Seminumerical algorithms
    Vol III: Sorting and searching
    Vol IV:

    Concrete Mathematics    PDF
    Graham / Knuth / Patashnik
*/
int *lista, n;
vector<int> v;

void mklst()
{
  cout << "Ingrese un numero: ";
  cin >> n;
  lista = new int[n];
  for(int i = 0; i < n; i++)
    lista[i] = -1;
}

void imprimir()
{
  for(int i = 0; i < v.size(); i++)
    cout << v[i] << " ";
  cout << endl;
  v.pop_back();
}

bool distinto(int k)
{
  for(int i = 0; i < v.size(); i++)
      if(v[i] == k)
        return false;
  return true;
}

void permutacion()
{
  for(int i = 1; i <= n; i++)
    if(distinto(i))
    {
      v.push_back(i);
      if(v.size() < n)
        permutacion();
      else
        imprimir();
    }
  v.pop_back();
}

void permutacion(int k)
{
  v.push_back(k);
  permutacion();
}

int main()
{
  cin >> n;
  for(int i = 1; i <= n; i++)
    permutacion(i);
  /*mklst();
  permutacion(0);*/
  /*
  n = 3;
  for(int i = 1; i <= n; i++)
    for(int j = 1; j <= n; j++)
      if(j != i)
        for(int k = 1; k <= n; k++)
          if(k != i && k != j)
            cout << i << j << k << endl;*/
  return 0;
}