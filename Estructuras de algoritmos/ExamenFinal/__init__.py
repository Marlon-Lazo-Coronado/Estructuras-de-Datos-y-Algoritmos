import numpy as np
import pandas as pd
import prince
import mglearn


import matplotlib.pyplot as plt
import seaborn as sns

from   sklearn.cluster import KMeans

class ProceseArchivo():
    def CargarArchivo(self,nombrearchivo):
        self.__df=pd.read_csv(nombrearchivo, delimiter=',',decimal=".")    
        return True  
  
    def ReducirDataFrame(self,columnas):
        df_reducido=self.__df.drop(  self.__df.columns[columnas],axis=1)
        return df_reducido
  
    def VisualizarDatos(self):
        print("Contenido de archivo leido")
        print(self.__df.iloc[0:8,0:5])
        print("\nNombres de las columnas (variables)")
        print(self.__df.columns)
        print("\nNombres de los primeros 10 paises")
        nombres=self.__df.iloc[:,1]
        print(nombres[0:10])
  
    def ProcesarDatos(self,NombreArchivo,Indice,ColumnasBorrar):
        if not self.CargarArchivo(NombreArchivo):
            return False
        self.VisualizarDatos()
        df_reducido=self.ReducirDataFrame(ColumnasBorrar)  
        df_reducido=df_reducido.set_index(Indice)
        #
        df_reducido=df_reducido.diff(axis=1)
        df_reducido=df_reducido.drop(df_reducido.columns[0],axis=1)
        #
        df_reducido=df_reducido.groupby(df_reducido.index).agg(lambda m:sum(m))
        #print(df_reducido)
        return df_reducido
    
    
    
Procesar=ProceseArchivo()
indice="Country/Region"
ColumnsToDelete=[0]+ list(range(2,4))    # Se eliminaran en todos los archivos las columnas 0,2,3
DF=Procesar.ProcesarDatos(r"\Users\mlazo\OneDrive\Escritorio\EstructurasDeAlgoritmos\IE0217_Tabajos_Fix\IE0217_Trabajos\ExamenFinal\Data\time_series_covid19_recovered_global.csv",indice,ColumnsToDelete)
print(DF)


paises = ['Peru', 'Chile', 'Paraguay', 'Uruguay', 'Brazil', 'Colombia', 'Venezuela', 'Ecuador', 'Argentina', 'Bolivia']
#Pequenio metodo para seleccionar los paises mediante una 
def Tabla_reducida(tabla, A):
    #Localizamos los paises
    Tabla_reducida = tabla.loc[A, :]
    return Tabla_reducida;
    
tabla_filtrada = Tabla_reducida(DF, paises)
print("\nla tabla con los paises seleccionasdos es: \n", tabla_filtrada)


def k_medias(tabla_filtrada):
    #Acemos la transpuesta
    Tabla_T = tabla_filtrada.T#Covid_selected.T
    #print("\nTabla transpuesta:\n", Tabla_T)
    # Construye un modelo k-medias
    kmedias = KMeans(n_clusters=3)
    # Cluster al que pertenece al que asigna k-medias
    kmedias.fit(Tabla_T)
    #Tabla
    print("\nDatos: \n", kmedias.predict(Tabla_T))
    #Centros
    centros = np.array(kmedias.cluster_centers_)
    print("\nLos centros son: \n", centros)
    #Ploteamos
    paleta = ['#CF8EF8', '#523C81', '#D2D132', '#59C951', '#E5826C','#A34F55','#CF8AF8','#723E81','#D6A132','#51B951']
    plt.figure(1,figsize=(10,8))
    #Plotea Centro 1
    plt.subplot(1, 1, 1)
    y  = centros[:1, :].tolist()[0]
    plt.bar(range(len(y)), y, 1/1.5, color=paleta)
    plt.xticks(range(Tabla_T.shape[1]), Tabla_T.columns)
    plt.show()
    
    # Plotea Centro 2
    fig = plt.figure()
    y= centros[1:2, :].tolist()[0]
    plt.bar(range(len(y)), y, 1/1.5, color=paleta)
    plt.xticks(range(Tabla_T.shape[1]), Tabla_T.columns)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.show()

    # Plotea Centro 3
    fig = plt.figure()
    y = centros[2:3, :].tolist()[0]
    plt.bar(range(len(y)), y, 1/1.5, color=paleta)
    plt.xticks(range(Tabla_T.shape[1]), Tabla_T.columns)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.show()
k_medias(tabla_filtrada)

###################################################################################################################
#Obtenemos filas mes y anio
def agregar_col(tabla_dif):
    meses = pd.DatetimeIndex(tabla_dif.index).month
    tabla_dif = tabla_dif.assign(month_x = meses)
    anios = pd.DatetimeIndex(tabla_dif.index).year
    tabla_dif = tabla_dif.assign(year_x = anios)
    return tabla_dif

##############################################################################
#Obtenemos los paises solicitados
tabla_filtrada = Tabla_reducida(DF, paises)
#Transponemos
tabla_T = tabla_filtrada.T
#Obtenemos la diferencia
tabla_dif = tabla_T.diff()
#Obtenemos columnas de meses y anios
separada = agregar_col(tabla_T)
#Agrupamos por mes y anio y calculamos la media
F = separada.groupby(['month_x', 'year_x']).mean()
print("\nLa media por anio y mes es: \n", F)
##############################################################################

#Repetimos el metodo porque estaba dando un poco de problemas porque decia que los ejes se repetian
def k_medias2(Tabla_final):
    # Construye un modelo k-medias
    kmedias = KMeans(n_clusters=3)
    # Cluster al que pertenece al que asigna k-medias
    kmedias.fit(Tabla_final)
    #Tabla
    print("\nDatos: \n", kmedias.predict(Tabla_final))
    #Centros
    centros2 = np.array(kmedias.cluster_centers_)
    print("\nLos centros son: \n", centros2)
    #Ploteamos
    paleta2 = ['#CF8EF8', '#523C81', '#D2D132', '#59C951', '#E5826C','#A34F55','#CF8AF8','#723E81','#D6A132','#51B951']
    fig = plt.figure()
    #Plotea Centro 1
    X  = centros2[:1, :].tolist()[0]
    plt.bar(range(len(X)), X, 1/1.5, color=paleta2)
    plt.xticks(range(Tabla_final.shape[1]), Tabla_final.columns)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.show()
    
    # Plotea Centro 2
    fig = plt.figure()
    #plt.subplot(1, 3, 2)
    X= centros2[1:2, :].tolist()[0]
    plt.bar(range(len(X)), X, 1/1.5, color=paleta2)
    plt.xticks(range(Tabla_final.shape[1]), Tabla_final.columns)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.show()

    # Plotea Centro 3
    fig = plt.figure()
    #plt.subplot(1, 4, 3)
    X = centros2[2:3, :].tolist()[0]
    plt.bar(range(len(X)), X, 1/1.5, color=paleta2)
    plt.xticks(range(Tabla_final.shape[1]), Tabla_final.columns)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.show()    

#Le pasamos la tabla procesada
k_medias2(F)
######################################################################################################################
#Esta parte la hicimos en la tarea, se utilizo el codigo que ya se habia hecho
#grafico boxplot
fig = plt.figure()
normalizado = F.groupby(['month_x', 'year_x']).sum()
normalizado.boxplot()
fig.set_figheight(6)
fig.set_figwidth(10)
plt.show()
    
#Normalizamos
normalizado=normalizado.apply(lambda x : x/max(x))
print(normalizado)
df_small = normalizado.iloc[:,:10]
correlation_mat = df_small.corr() #Obtenemos matriz de correlacion
print(correlation_mat)
        
#Graficamos correlacion
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_mat, mask=np.zeros_like(correlation_mat), cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax)
plt.show()
    
    
    