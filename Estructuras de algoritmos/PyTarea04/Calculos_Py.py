import numpy as np


#================================== 1. ==================================================================================================
print("\n\n1.................................................................\n")
x = np.array([3,9,20,13,50,89])
y = np.array([20,3,67,80])
#Utilizando las funciones de numpy
print("Para la variable y los calculos estadisticos son:")
print("Media: ",y.mean()) #Media
print("Desviacion estandar: ", y.std()) #Desviacion
print("Mediana", np.median(y)) #Mediana

print("\nPara la variable x los calculos estadisticos son:")
print("Media: ",x.mean()) #Media
print("Desviacion estandar: ", x.std()) #Desviacion
print("Mediana", np.median(x)) #Mediana

#Calculo de mediana mediante un for para  x.
z = 0.5;
s = 0;
m = 0;
for i in x:
    s = s + i;
    m = x[int(len(x)/2)];
if type(z) != type(len(x)/2):
    print("\n\nLa mediana calculada a mano es: ",m);
else: 
    m = (x[int(len(x)/2)-1] + x[int(len(x)/2)])/2; #len()/2 se me estaba haciendo en flotante, que vulgar!
    print("\nLa mediana de x calculada a mano es: ",m)

'''
x= [3,9,20,13,50,89] 
y={20,3,67,80}

X = pd.DataFrame(x)
Y = pd.DataFrame(y)

print(len(Y)) #Con esto obtengo la logitud de la lista

for i in X.index:
   
    print(X[0][i]+1)
int(Y[0:4]) De esta forma podemos acceder a los datos!'''

