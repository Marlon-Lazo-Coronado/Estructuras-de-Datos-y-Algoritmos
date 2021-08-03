#include <iostream>
#include<stdlib.h>
#include<time.h>
#include "encabezado.h"

using namespace std;

void ordenar ( float *vector, int n){

float tem;

for(int i = 0; i < n; i = i + 1)
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
    }

}
