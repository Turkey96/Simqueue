import re
import pandas as pd
values = [[], [], [], [], [], []]
with open("data.txt", "r") as dataset:
  for d in dataset.readlines():
    for i in [0,2]: 
        values[i].append(float(re.findall(r"[\d]+.[\d]+", d)[0 if i == 0 else 1]))
#Obtenemos el numero de trabajos usando la funcion len
n = len(values[0])
#Se asume que los valores iniciales son 0
c = 0.0
i = 0
#Mientras haya trabajos
while i < n:
  i += 1
  #Tiempo en el que llega el trabajo o proceso
  a = values[0][i - 1]
  #En caso de que aun no haya terminado trabajo previo se calcula el retraso
  if a < c: d = c - a
  #De lo contrario el retraso es 0
  else:     d = 0.0
  #Se definen:
  #Tiempo de servicio
  s = values[2][i - 1]
  #Tiempo de salida
  c = a + d + s
  #Tiempo en que inicia el servicio
  b = a + d
  #Tiempo de espera en el nodo
  w = d + s
  #Se adjunta valores en la matriz
  values[1].append(d)
  values[3].append(b)
  values[4].append(c)
  values[5].append(w)
#Se usa la funcion round o redondeo para que los datos estadisticos no sean tan "descomunales"
#Se calcula el tiempo promedio entre llegadas
ar = round(a / n,5)
#Se calcula el tiempo promedio de servicio
ps = round(sum(values[2]) / n,5)
#Se calcula el tiempo promedio de retraso
ad = round(sum(values[1]) / n,5)
#Se calcula el tiempo promedio de espera
aw = round(sum(values[5]) / n,5)
#Se calcula la tasa de llegada
rt = round(1 / ar,5)
#Se calcula la tasa de servicios
st = round(1 / ps,5)
#Se calcula el numero promedio de tiempo en el nodo
l = round((n / c) * aw,5)
#Se calcula el numero promedio de tiempo en la cola
q = round((n / c) * ad,5)
#Se calcula el numero promedio de tiempo en la cola
x = round((n / c) * ps,5)
#Impresion de los datos
#Se intenta mostrar los valores estadisticos de cada trabajo, lo cual en la terminal se mostraran los ultimos por su extension
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    Titulo0="Estadisticas de cada trabajo"
    print(Titulo0.center(100,"="))
    print(pd.DataFrame(values, index=["Llegada(a)", "Retraso(d)", "Servicio(s)", "InicioS(b)", "Salida(c)", "Espera(w)"], columns=[i for i in range(1,1001)]))
Titulo1="Estadisticas promedio de trabajo"
print(Titulo1.center(100,"="))
subt="en s/t (segundos por trabajo)"
print(subt.center(100," "))
print("Tiempo medio de llegada(ar):",ar)
print("Tiempo medio de servicio(ps):",ps)
print("Tiempo medio de retraso(ad):",ad)
print("Tiempo medio de espera(aw):",aw)
subt2="en t/s (trabajos por segundo)"
print(subt2.center(100," "))
print("Tasa de llegada(rt):",rt)
print("Tasa de servicios(st):",st)
if ar > ps: 
    print("El servidor puede realizar los trabajos a medida que estos llegan")
else: 
    print("El servidor no puede realizar los trabajos a medida que estos llegan")
Titulo2="Estadisticos de tiempo"
print(Titulo2.center(100,"="))
print("Promedio de tiempo en el nodo:(l)",l)
print("Promedio de tiempo en la cola(q):",q)
print("Promedio de tiempo en el servidor(x):",x)
print("Consistencia:","Correcta" if round(l,5) == round(q + x,5) else "Incorrecta")