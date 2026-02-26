
import random

MIN = 32   # primer carácter visible (espacio)
MAX = 126  # último carácter visible (~)
RANGO = MAX - MIN + 1

welcome_message = """

//////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////// BIENVENIDO AL ENCRIPTADOR/DESENCRIPTADOR DE MENSAJES //////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
Este programa te permite encriptar y desencriptar mensajes utilizando un método de desplazamiento
 de caracteres.

Al encriptar, se generará un número aleatorio entre 1 y 94 (el rango de caracteres visibles) que se
 utilizará como desplazamiento para cada carácter del mensaje.

És similar al cifrado César, pero con un rango de caracteres más amplio.

Diviertete encriptando y desencriptando tus mensajes, ¡y recuerda guardar el número de desplazamiento 
para poder desencriptar correctamente!
//////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////


 """
print(welcome_message)
select = input("¿Deseas encriptar o desencriptar un mensaje? (E/D): ").lower()

if select == "e":
    n = random.randint(1, RANGO - 1)
    mssg = input("Inserta el mensaje a encriptar: ")
    encrypted_mssg = ""

    #Recorremos cada carácter del mensaje, obtenemos su código ASCII y aplicamos el desplazamiento teniendo en cuenta el rango de caracteres visibles. Si el carácter no es visible, lo dejamos sin cambios.
    for c in mssg:
        code = ord(c)
        if MIN <= code <= MAX:
            encrypted_mssg += chr((code - MIN + n) % RANGO + MIN)
        else:
            encrypted_mssg += c

    print(f"El mensaje encriptado es: {encrypted_mssg}")
    print(f"El número de desplazamiento es: {n}")

elif select == "d":
    n = int(input("Inserta el número de desplazamiento (1-94): "))
    encrypted_mssg = input("Inserta el mensaje encriptado: ")
    mssg = ""
    
    #Recorremos cada carácter del mensaje encriptado, obtenemos su código ASCII y aplicamos el desplazamiento inverso teniendo en cuenta el rango de caracteres visibles. Si el carácter no es visible, lo dejamos sin cambios.
    for c in encrypted_mssg:
        code = ord(c)
        if MIN <= code <= MAX:
            mssg += chr((code - MIN - n) % RANGO + MIN)
        else:
            mssg += c

    print(f"El mensaje desencriptado es: {mssg}")



