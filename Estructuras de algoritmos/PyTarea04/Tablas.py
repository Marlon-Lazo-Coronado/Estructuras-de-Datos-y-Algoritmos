import pandas as pd
from numpy import mean,std


print("\n\n2.................................................................\n")
datos = {'nombre': ["John","Paul","George","Michael","Markus","Eduard","Jimmy"],
         'ciudad': ["Liverpool","New York","London","Paris","Madrid","Kansas", "San Jos"],
         'Edad': [20,30,22,55,65,52,33]
         }
tabla = pd.DataFrame(datos)
#vector = tabla.loc[:,'Edad']
#vector = tabla.to_numpy(vector)
#Tabla2=tabla.to_string(header=False) #Para remover columnas
#vector = tabla.to_numpy(tabla[2:])
print("\nLa tabla es: \n")
print(tabla)
print("\nLa media de edad es: ",std(tabla.loc[:,'Edad']),"\nLa desviacion estandar de edad es: ", mean(tabla.loc[:,'Edad']))

#Ordenamos por la columna nombres.
orden1 = tabla.sort_values('nombre')
print("\nOrdenamos por la columna nombres. \n")
print(orden1)
print("\nOrdenamos por la columna ciudad. \n")
orden1 = tabla.sort_values('ciudad', ascending=True)
print(orden1)