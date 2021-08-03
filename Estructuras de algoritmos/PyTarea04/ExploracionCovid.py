import os
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
#A
def CargarArchivo(nombre_archivo):
    #Se copia la direccion del directorio actual
    directorio_actual=os.getcwd()
    print("\n\nLas direcciones con las que se trabaja son:\n")
    print(directorio_actual)
    #Se cambia la directorio del archivo para poder accederlo, la r es porque si no python entiende la direccion ente '' como cadena de caracteres
    os.chdir(r"\Users\mlazo\OneDrive\Escritorio\EstructurasDeAlgoritmos\SmartGitReservorio\Semana05\Clase15\Datos")
    #os.chdir(r"direccion_directorio")
    print(os.getcwd())
    datos_est = pd.read_csv(nombre_archivo,delimiter=',',decimal=".")
    #Volvemos al directorio actual
    os.chdir(directorio_actual)
    print(os.getcwd())
    #B Y C, Rcortamos el datafreme(la tabla)
    del(datos_est['Province/State'])
    del(datos_est['Lat'])
    del(datos_est['Long'])
    return datos_est;


def Tabla_reducida(A,nombre_archivo):#
    Tabla = CargarArchivo(nombre_archivo) # Cargamos el archivo y lo copiamos (La tabla sin Province/State, Lat, Long)
    print("\n\nLa tabla cargada y sin Province/State, Lat, Long es:\n")
    print(Tabla)
    Tabla_indexada = Tabla.set_index('Country/Region');    #Convertimos el la columna Country/Region en el indice
    print('\nLa tabla idexada es: \n')
    print(Tabla_indexada)
    Tabla.rename(columns={'Country/Region':'Country'}, inplace=True) #Le cambiamos el nombre a Country/Region por Country porque el / da problemas
    #tabla_reducida = Tabla.index.get_indexer(A)
    #tabla_reducida = Tabla[Tabla.indexer(A)]
    tabla_reducida = Tabla[Tabla.Country.isin(A)]                    #Filtramos la tabla con la lista de paises A[]
    #tabla_reducida = Tabla.loc[tabla['Country/Region']=='Spain']
    print('\nLa tabla reducida con la lista es: \n')
    print(tabla_reducida)
    return tabla_reducida;


def grafica(tabla_graficar):
    #CREACION DE LA LISTA DE NUMEROS
    B = [];
    for i in range(len(tabla_graficar.columns)): #Tiene tama_no del numero de columans menos el campo del pais, por eso se le hace pop a la pocicion cero abajo
        B.append(i)
        i = i +1;
    B.pop(0)
    #CREACION DE LAS LISTA DE DATOS
    #La tabla se convirtio en una lista que contiene los campos como listas, por eso despues se le hace pop a la primera posicion que contiene la lista de fechas
    lista_productos = [tabla_graficar.columns.values.tolist ()] + tabla_graficar.values.tolist()  #Convertimos a lista de listas
    lista_productos.pop(0) #Se remueven la fila de fechas!
    #NOMBRE DE LOS PAISES
    for i in range(len(tabla_graficar.index)): #Grsficamos tantas como indices hayan
        tem = lista_productos[i];              #Se obtiene la lista del pais i
        nombre = tem[0];                       #Se le copia el nombre
        tem.pop(0)                             #Se le elimina el nombre para tener solo numeros
        #Graficamos todos los paises
        plt.plot(B,tem,label=nombre)
        plt.xlabel('Numero de dias')
        plt.ylabel('Cantidad de reportados')
        plt.title("reportes Covid-19")
        plt.legend()
        #plt.savefig('grafica_lineal.png')
    plt.show() #En el for se cargan todas las graficas y al final se muestran
    #GRAFICACION





def Analice_archivo(nombre_archivo):
    nombre_archivo_tranas = os.path.join(nombre_archivo) #Tomamos el nombre del archivo y lo hacemos en una direccion
    paises = ['Costa Rica', 'Panama', 'Colombia', 'Spain', 'Italy', 'Mexico', 'Germany']
    tabla_fechas = Tabla_reducida(paises,nombre_archivo_tranas); #Funcion que devuelve la tabla recortada
    grafica(tabla_fechas)                  #Graficacion de la rabla recortada
    
#La funcion se puede generalizar mas pasandoles la direccion del directorio, pero de todos modos la funcion esta hecha para una tabla con el formato de la tabla covi, entonces no tiene mucha gracia.
Analice_archivo('time_series_covid19_confirmed_global.csv')
Analice_archivo('time_series_covid19_deaths_global.csv')
Analice_archivo('time_series_covid19_recovered_global.csv')







