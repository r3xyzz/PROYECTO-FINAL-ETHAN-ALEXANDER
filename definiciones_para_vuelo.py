def mostrar_asiento_disponible():
    print("asientos disponibles: ")
    for e in range(1, 43):
        if e in asientos_ocupados:
            print