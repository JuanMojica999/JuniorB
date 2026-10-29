#Crea un programa con las variables edad y tiene_entrada. 
# El programa debe permitir el acceso únicamente si la persona tiene 16 años o más y tiene una entrada. 
# Si no cumple ambas condiciones, debe indicar que no puede ingresar.

edad = int(input("¿Cuál es tu edad? "))
tiene_entrada = input("¿Tienes entrada? (si/no): ")

if edad >= 16 and tiene_entrada == "si":
    print("Puedes ingresar")
else:
    print("No puedes ingresar")