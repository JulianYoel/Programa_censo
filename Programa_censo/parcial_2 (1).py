 
#Se pide calcular e informar lo siguiente:  
# Nombre del jefe/a de familia con la mayor cantidad de caracteres (o sea, el nombre más 
#largo) 
 




# Exportar toda la información a un archivo csv. 

numeroHogar = 0
personasCensadas = 0
jefx = 0
menores18 = 0
mayores65 = 0
personaVieja = 0
personaJoven = 0
ingresos = 0
vehiculo = 0
vivienda = 0
m2 = 0
personasSolas = 0
censo = []
sinAuto = 0
totalMenores18 = 0
vivienda = 0
salarioMasBajo = 1000000
depto = 0

integr = int(input("miembros del grupo familiar: "))

while (integr != 0):
    
    jefx = input("¿cual es el nombre del jefe/a de la familia?: ")
    menores18 = int(input("¿cuántos menores de 18 años hay en el grupo familiar?: "))
    mayores65 = int(input("¿cuantos mayores de 65 años posee el grupo familñiar?: "))
    personaVieja = int(input("¿qué edad tiene la persona de mayor edad del grupo familiar?: "))
    personaJoven = int(input("¿que edad tiene la persona mas joven del grupo familiar?: "))
    ingresos = float(input("¿cuánto es el ingreso salarial total del grupo familiar?: "))
    vivienda = input("tipo de vivienda departamento/casa: ")
    if vivienda == "departamento":
       m2 = float(input("¿cuantos metros cuadrados tiene el departamento?: "))
    else:
        vivienda = "casa"
        
    vehiculo = input("cantidad de vehiculos que posee el grupo familiar: ")
    if vehiculo == 0:
        sinAuto = vehiculo + 1
   
    personasCensadas = personasCensadas + integr
    numeroHogar = numeroHogar +1
    totalMenores18 = totalMenores18 + menores18
    
    if ingresos < salarioMasBajo:
        salarioMasBajo = ingresos
    
    
    if integr == 1:
        personasSolas = personasSolas + 1
    
    if vivienda == "departamento":
        depto = depto + 1
   
            
    integr = int(input("miembros del grupo familiar: "))
           
    dato = {
            "jefx": " ",
            "menores18": " ",
            "mayores65": " ",
            "personaVieja": " ",
            "personaJoven": " ",
            "ingresos": " ",
            "vivienda": " ",
            "m2": " " ,
            "sinAuto": " ",
        }
    
    dato["jefx"] = jefx
    dato["menores18"] = menores18
    dato["mayores65"] = mayores65
    dato["personaVieja"] = personaVieja
    dato["personaJoven"] = personaJoven
    dato["ingresos"] = ingresos
    dato["vivienda"] = vivienda
    dato["m2"] = m2
    dato["sinAuto"] = sinAuto
    
    
    
    censo.append(dato)

for listaOrdenada in censo:

    print(listaOrdenada)
    
#PROCESAMIENTO DE DATOS

#Cantidad de habitantes censados.

print("la cantidad de personas censadas es de: {}".format(personasCensadas))
    
#Nombre del jefe/a de familia con la mayor cantidad de caracteres (o sea, el nombre más 
#largo)

len(listaOrdenada)
print(jefx)
#cantidad de personas de viven solas. 

print("{} personas viven solas".format(personasSolas))

#Porcentaje de viviendas donde viven personas solas.
from funciones.py import porcentaje
porcPerSolas = porcentaje(100,personasSolas, numeroHogar)
print("porcentaje de viviendas con personas solas es {} %".format(porcPerSolas))

# Cantidad de menores de 18 años registrados en el censo.
print("el total de menores de 18 años censados es de {} personas".format(totalMenores18))

# Informar el salario familiar registrado más bajo. 
print("el salario ams bajo registrado es de {} pesos".format(salarioMasBajo))

# Informar cuantas familias no tienen vehículos. 
print("{} familias no poseen auto".format(sinAuto))

# Informar cuantas familias viven en departamentos y el promedio de metros cuadrados. 
from funciones.py import promedio

promM2= promedio(m2, depto)

print("{} personas viven en departamento".format(depto))
print("y el tamaño de departamento promedio es de {} m2".format(promM2))








