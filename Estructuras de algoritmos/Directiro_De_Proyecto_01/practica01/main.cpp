#include <iostream>
#include<stdlib.h>
#include<time.h>
#include "encabezado.h"


using namespace std;

int main()
{
    int n;
    cout << "Ingrese el tamaño del vector" << endl;
    cin >> n;

    float *vector;
    float tem;
    vector = new float [n];
    cout << "El vector a ordenar es: " << endl ;

    for(int i = 0; i < n; i = i + 1)
    {
       vector[i]=rand()%101;
       cout << " " << vector[i];
    }

    ordenar(vector, n);









    /////////////////////////////////////////////////////////////////


    /*for(int i = 0; i < n; i = i + 1)
    {
        for(int j = 0; j < n; j = j + 1){
            if(vector[i]<vector[j])
                {
                    tem = vector[i];
                    vector[i] = vector[j];
                    vector[j] = tem;
                }
        }
    }

    cout << endl << "El vector ordenado es: " << endl;

    for(int i = 0; i < n; i = i + 1)
    {
       cout << " " << vector[i];
    }*/

    return 0;
}
