# RAMA ETHAN
# RAMA ALEX
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
Comprar asiento: Solicita los datos del usuario, luego el usuario escoge un asiento, si es usuario de /bancoduoc/ el sistema 
======================================================================================================================
'''
# Definición de variables globales
asientos_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
asientos_ocupados = []
precios = {
    'normal': 78900,
    'vip': 240000
}
datos_pasajeros = {}


print("/////////////////////////")
print("Bienvenido a Vuelos-Duoc")
print("/////////////////////////")
print()

# Función para mostrar los asientos disponibles
def mostrar_asientos_disponibles():
    print("Asientos disponibles:")
    print("Recalcar que los precios de los asiento del 1 al 30 *normal* y del 31 al 42 *vip*")
    for i in range(1, 43):
        if i in asientos_ocupados:
            print("X", end=" ")
        else:
            print(i, end=" ")
        if i % 6 == 0:
            print()

# Función para comprar un asiento
def comprar_asiento():
    nombre = input("Ingrese el nombre del pasajero: ")
    rut = input("Ingrese el RUT del pasajero: ")
    telefono = input("Ingrese el teléfono del pasajero: ")
    banco = input("Ingrese el banco del pasajero: ")

    try:
        print("Seleccione un asiento:")
        mostrar_asientos_disponibles()
        seleccion = int(input("Ingrese el número de asiento: "))

        if seleccion in asientos_ocupados:
            print("El asiento seleccionado ya está ocupado.")
            return

        if banco.lower() == "bancoduoc" and (seleccion < 31 or seleccion > 42):
            print("Los usuarios de BancoDuoc deben elegir un asiento VIP.")
            return

        if seleccion >= 31 and seleccion <= 42:
            precio = precios['vip']
        else:
            precio = precios['normal']

        if banco.lower() == "bancoduoc":
            descuento = precio * 0.15
            precio -= descuento

        print("El valor del asiento seleccionado es: $" + str(precio))
        confirmacion = input("¿Desea confirmar la compra? (s/n): ")

        if confirmacion.lower() == 's':
            asientos_disponibles.remove(seleccion)
            asientos_ocupados.append(seleccion)
            datos_pasajeros[seleccion] = {
                'nombre': nombre,
                'rut': rut,
                'telefono': telefono,
                'banco': banco
            }
            print("Compra realizada con éxito.")
        else:
            print("Compra cancelada.")
    except ValueError:
        print("Error: ¡Ingrese un número de asiento válido!")

#La funcion para anular un vuelo
def anular_vuelo():
    try:
        seleccion = int(input("Ingrese el número de asiento a anular: "))

        if seleccion in asientos_ocupados:
            asientos_ocupados.remove(seleccion)
            asientos_disponibles.append(seleccion)
            del datos_pasajeros[seleccion]
            print("Vuelo anulado con éxito.")
        else:
            print("El asiento seleccionado no está ocupado.")
    except ValueError:
        print("Error: ¡Ingrese un número de asiento válido!")

# Función para modificar datos de pasajero (esepcificar asiento de pasajero con asiento comprado para hacer el cambio de informacion de pasajero)
def modificar_datos_pasajero():
    try:
        seleccion = int(input("Ingrese el número de asiento a modificar: "))

        if seleccion in datos_pasajeros:
            print("Datos actuales:")
            print("Nombre: ", datos_pasajeros[seleccion]['nombre'])
            print("RUT: ", datos_pasajeros[seleccion]['rut'])
            print("Teléfono: ", datos_pasajeros[seleccion]['telefono'])
            print("Banco: ", datos_pasajeros[seleccion]['banco'])

            nombre = input("Ingrese el nuevo nombre del pasajero: ")
            rut = input("Ingrese el nuevo RUT del pasajero: ")
            telefono = input("Ingrese el nuevo teléfono del pasajero: ")
            banco = input("Ingrese el nuevo banco del pasajero: ")

            datos_pasajeros[seleccion]['nombre'] = nombre
            datos_pasajeros[seleccion]['rut'] = rut
            datos_pasajeros[seleccion]['telefono'] = telefono
            datos_pasajeros[seleccion]['banco'] = banco

            print("Datos modificados con éxito.")
        else:
            print("El asiento seleccionado está vacío.")
    except ValueError:
        print("Error: ¡Ingrese un número de asiento válido!")

#Esto va a ejecutar el programa de vuelo
while True:
    print("\nBienvenido a Vuelos-Duoc")
    print("Seleccione una opción:")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")