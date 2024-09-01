# Detención de Palíndromos: 

#Es lo que en Argentina llamamos palabra 'capicua', vale decir, que se lee de la misma forma ya sea de izquierda a derecha o derecha a izquierda



#1) Pedimos al usuario nos coloque la palabra a evaluar: 
cadena = input("Por favor, introduce una cadena: ")

#Esta es una funcion para que pase todo el string a minúsculas, sea cual fuere el tipo de letra con el que escribe el usuario:

cadena = cadena.lower()

#Transformamos esa texto en una lista:
l_cadena = list(cadena)

#Ahora damos vuelta la lista:
l_cadena_al_Reves = list(cadena)
l_cadena_al_Reves.reverse()

#sacamos los espacios entre las palabras de una oracion:
while " " in l_cadena:
    l_cadena.remove(" ")

while " " in l_cadena_al_Reves:
    l_cadena_al_Reves.remove(" ")



#y damos la sentencia de como deberia ser:
if l_cadena == l_cadena_al_Reves:
    print("La palabra introducida es un palondromo, o sea, es capicua.")
else:
    print("La palabra introducida NO es un palindromo, no es capicua.")
