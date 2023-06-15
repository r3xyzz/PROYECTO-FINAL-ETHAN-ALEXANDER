'''
ENUNCIADO
--Vuelos-Duoc requiere contratar sus servicios de informática para el desarrollo de un proyecto en Python, el cual consiste en la
venta de sus pasajes.
El sistema debe considerar que se encuentran disponibles un total de 42 asientos por avión, ver ejemplo:
======================================================================================================================
| 1 2 3 4 5 6 |
| |
| 7 8 9 10 11 12 |
| |
| 13 14 15 16 17 18 |
| |
| 19 20 21 22 23 24 |
| |
| 25 26 27 28 29 30 |
|______________________ ________________________|
|______________________ ________________________|
| 31 32 33 34 35 36 |
| |
| |
| 37 38 39 40 41 42 |
======================================================================================================================
Dentro de las restricciones, se contempla que desde el asiento 31 al 42 son para pasajeros vip.
Los precios son:
* Asiento normal, $78.900
* Asiento vip, $240.000.

-El sistema debe permitir al usuario:
* Seleccionar un asiento disponible (mostrando los que aún tienen disponibilidad)
* Indicar el valor, una vez que el usuario lo acepte.
Además, solicitar los siguientes datos del usuario:
* nombrePasajero
* rutPasajero
* telefonoPasajero
* bancoPasajero
Se pide implementar el siguiente menú:
1. Ver asientos disponibles
2. Comprar asiento
3. Anular vuelo
4. Modificar datos de pasajero
5. Salir
======================================================================================================================
--Ver asientos disponibles: Mostrará por pantalla todos los asientos disponibles con su número de asiento y los no
disponibles los con una “X”
| 1 2 3 4 5 6                                   |
|                                               |
| 7 X X 10 11 12                                |
|                                               |
| X X X 16 X 18                                 |
|                                               |
| 19 20 21 22 23 24                             |
|                                               |
| 25 26 27 X 29 30                              |
|______________________ ________________________|
|______________________ ________________________|
| X 32 33 34 35 36                              |
|                                               |
|                                               |
| X 38 X 40 41 X                                |
Comprar asiento: Solicita los datos del usuario, luego el usuario escoge un asiento, si es usuario de “bancoDuoc” el sistema 
======================================================================================================================
'''
#Definicion de los numeros de asientos ocupados y disponibles, ademas de su respectivos precios
asientos_disponibles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]
asientos_ocupados = []
precio = {
    'normal': 78900,
    'vip': 240000,
}
#Definicion de datos de pasajeros
datos_pasajero = {}

print("/////////////////////////")
print("Bienvenido a Vuelos-Duoc")
print("Gracias por Preferirnos")
print("/////////////////////////")
print()

def mostrar_asiento_disponible():
    print("asientos disponibles: ")
    for e in range(1, 43):
        if e in asientos_ocupados:
            print("X", end=" ")
        else:
            print(e, end=" ")
        if e % 6 == 0:
            print()

#Definiendo la funcion para comprar un asiento
def comprar_asiento():
    nombre = input("Ingrese el Nombre del pasajero: ")
    rut = input("Ingrese el RUT del pasajero: ")
    telefono = input("Ingrese el Telefono del pasajero: ")
    banco =input("Ingrese el Banco del pasajero: ")

    print("Seleccione un asiento a su preferencia: ")
    mostrar_asiento_disponible()
    seleccion = int(input("Ingrese el numero del asiento: "))
    