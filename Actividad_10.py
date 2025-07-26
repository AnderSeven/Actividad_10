opciones = 0
a = False
while a == False:
    print("====Menu de retos recursivos===")
    print("1. Invertir una cadena de texto")
    print("2. Calcular la suma de los primeros N numeros naturales")
    print("3. Imprimir una cuenta regresiva desde N hasta 1")
    print("4. Sumar los digitos de un numero")
    print("5. Contar cuantos digitos tiene un numero")
    print("6. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            print("asf")
        case 2:
            print("asdf")
        case 3:
            print("adsf")
        case 4:
            print("asdf")
        case 5:
            print("asdf")
        case 6:
            print("Gracias por usar el sistema...")
            a = True
        case _:
            print("Opcion invalida")