#include <iostream>
#include <vector>
using namespace std;

int NMAX, MAXCNDTS, soluciones = 0;
bool finished = false;

bool es_solucion(vector<int> a, int k, int n); //(a, k, input)
/*
Pregunta si los primeros k elementos de un
vector << a >> son una solucion completa de
un problema dado.
El ultimo argumento, input, nos permite pasar
informacion general dentro de la rutina. La usaremos para
espeficicar n, el tamaño de una solucion objetivo.
Esto tiene sentido cuando se contruyen permutaciones de
tamaño n, o subconjuntos de n elementos, pero puede que no
sea relevante cuando se construyen objetos de tamaño variable,
tal como un secuencia de movimientos de un juego.
En esas situaciones, el ultimo argumento no es necesario.
*/
void procesar_solucion(vector<int> a, int k);
/*
  Imprime, cuenta, o procesa una solucion completa una
  vez que es CONTRUIDA.
*/
//~~~~~~~~~CONSTRUIR CANDIDATOS~~~~~~~~~~~(a, k, input, c, cand)
void crt_cndts(vector<int> a, int k, int n, vector<int> &c, int &cand);
/*
  Llena un vector < c > con un conjunto completo de posibles candidatos
  para la k-esima posicion de < a >, dado el contenido de las primeras
  < k - 1 > posiciones. El numero de candidatos regresado en este
  vector esta dado por < cand >. De nuevo, input puede ser usada para
  pasar informacion auxiliar, particularmente el tamaño deseado de la
  solucion.
*/
//~~~~~~~~~ALGORITMO GENERAL~~~~~~~~~~~
void backtrack(vector<int> &a, int k, int n)
{
	vector<int> c(MAXCNDTS);
	int ncndts; //n-candidates
	if(es_solucion(a, k, n))
		procesar_solucion(a, k);
	else
	{
    //construct_candidates
		crt_cndts(a, k++, n, c, ncndts);
		for(int i = 0; i < ncndts; i++)
		{
			a[k - 1] = c[i];
			backtrack(a, k, n);
			if(finished)
				return;
		}
	}
}

bool es_solucion(vector<int> a, int k, int n){
    return true;
}
/*
  En el caso general, modelaremos nuestra solucion como un vector
  a = (a1, a2, ..., an), donde cada elemento ai es seleccionado de
  un conjunto finito ordenado < Si >. Tal vector podria representar
  un arreglo donde ai contiene el i-esimo elemento de la permutacion.

  O el vector podria representar un subconjunto S dado, donde ai
  es true si y solo si el i-esimo elemento del universo esta dentro
  de S.

  El vector incluso puede representar una secuencia de movimientos
  en un juego o el camino en un graph, donde ai contiene el i-esimo
  evento en la secuencia.

  En cada paso en el algoritmo, empezamos de una solucion parcial,
  sea, a = (a1, a2, ..., ak), e intentar extenderla agregando otro
  elemento al final. Despues de extenderla, debemos preguntar si
  lo que tenemos hasta ahora es una solucion -
*/

int main()
{
  int n;
	cin >> n;
	NMAX = n; //Puede cambiar
  MAXCNDTS = n; //Puede cambiar
  cout << "\n\nSoluciones: " << soluciones << endl;
  return 0;
}
