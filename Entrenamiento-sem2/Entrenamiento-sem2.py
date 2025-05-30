#   Determinar el estado de aprobación:
#       -Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#       -Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
#   Calcular el promedio:
#       -Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#       -Calcular y mostrar el promedio de las calificaciones en la lista
#   Contar calificaciones mayores:
#       -Preguntar al usuario por un valor específico
#       -Contar cuántas calificaciones en la lista son mayores que este valor
#   Verificar y contar calificaciones específicas:
#       -Preguntar al usuario por una calificación específica. 
#       -Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa. 
#
# ======================================//======================================

notas = [] # Se crea la lista notas la cual guardará notas para las funcionalidades del programa.

def agregar_nota(): # La definición de esta función será la utilizada para agregar notas a la lista.

    while True: # Se pide la nota al usuario y gracias a este ciclo, nos aseguramos que esté dentro del rango válido.

        try:
            
            nota = float(input("Digite la nota a agregar (0-100): "))
            if nota<0 or nota>100:
                print("Valor fuera de rango, intente de nuevo")  
                continue
            if nota>=70:
                print("Aprobó")
                break
            else:
                print("reprobó")
                break
        except ValueError: # Esta sentencia ayuda a que el programa no se detenga cuando el usuario ingrese un valor que no sea numérico.
            print("Valor inválido, intente de nuevo") # Al estar al final de un ciclo, esto hace que lo siguente sea volver a pedir la entrada hasta que sea válida.
      
    while True: # Se pregunta al usuario si desea guardar la nota ingresada.
        # Esta estructura es similar a la anterior, solo que al no tratarse de una entrada numerica, no es necesario utilizar la sentencia Try ya que esta admite cualquier tipo de entrada.
        
        guardar_nota = input("¿Desea guardar la nota en la lista?(S/N)\n").lower()

        if guardar_nota=="s":
            notas.append(nota)
            print("La nota ha sido agregada")
            break

        elif guardar_nota=="n":
            print("La nota no ha sido agregada")
            break
        
        else: # En este caso solo es necesario un camino en el condicional que indique que escribió una entrada no válida, el cual no rompa el ciclo para poder tomar de nuevo la entrada.
            print("Opción no válida, intente de nuevo")
        
def calcular_promedio(): # La definición de esta función nos ayuda a calcular el promedio de las notas contenidas en la lista.

    print("1. Promedio de las notas guardadas.\n2. Importar lista para promediar.")
    opcion_menu2 = int(input("Por favor digite la opción que desea elegir aquí: ---> "))
    # Se puede utilizar la lista ya guardada o importar una lista nueva.

    if opcion_menu2==1:

        promedio(notas)

    elif opcion_menu2==2:

        while True: # Estructura idéntica a la utilizada en el ingreso de notas solo que aquí ya de toman varias notas al mismo tiempo.
            entrada_notas = input("Por favor ingrese las notas separadas por comas:\n")

            try:
                user_notas_string = entrada_notas.split(",")
                user_notas_float = [float(x.strip()) for x in user_notas_string]

                if any(nota < 0 or nota > 100 for nota in user_notas_float):
                            print("Error: Todas las notas deben estar entre 0 y 100.")
                            continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar solo números válidos, separados por comas.")

        promedio(user_notas_float)

        while True: # Aquí se le permite al usuario guardar la nueva lista o no, la cual reemplazará la existente si hay alguna.

            guardar_notas = input("¿Desea guardar la lista y reemplazar la existente?(S/N)\n").lower()

            if guardar_notas=="s":
                notas [:]= user_notas_float
                print("La lista ha sido guardada")
                break

            elif guardar_notas=="n":
                print("La lista no ha sido guardada")
                break
            
            else: 
                print("Opción no válida, intente de nuevo")

def promedio(notas): # Función que se encarga de calcular el promedio de la lista que reciba (Ya sea la guardada o la que recién se ingresó).
    suma = sum(notas)
    if suma == 0:
        print("No hay notas para promediar")
    else:
        promedio = suma / len(notas)
        print("El promedio de las notas es:",promedio)

        
        

def comparar_notas(): # La definición de esta función nos ayuda a comparar qué notas son mayores/menores o iguales a la nota que el usuario ingrese.
    nota_referencia = float(input("Por favor ingrese la nota que desea comparar: "))

    # Se crean tres listas locales en donde se separan las notas de la lista inicial, según el parámetro ingresado.
    notas_mayores = [nota for nota in notas if nota > nota_referencia]
    notas_menores = [nota for nota in notas if nota < nota_referencia] 
    notas_iguales = [nota for nota in notas if nota == nota_referencia]

    cantidad_mayores = len(notas_mayores)
    cantidad_menores = len(notas_menores)
    cantidad_iguales = len(notas_iguales)

    # Se informa al usuario que cantidad de notas son mayores, menores e iguales a la nota ingresada y posteriormente cuáles son.
    print(f"La cantidad de notas mayores que {nota_referencia} son {cantidad_mayores}")
    print(f"La cantidad de notas menores que {nota_referencia} son {cantidad_menores}")
    print(f"La cantidad de notas iguales a {nota_referencia} son {cantidad_iguales}")

    print(f"Notas mayores: {notas_mayores}")
    print(f"Notas menores: {notas_menores}")

def consultar_nota(): # La definición de esta función nos permite mostrar al ususario qué notas hay en la lista guardada.

    for i in range(len(notas)): # Se utiliza esta estructura cíclica ya que queremos imprimir todas las notas contenidas sin importar la cantidad que sean.
        print(f"La nota {i+1}. es  {notas[i]}")

def main():  # La definición de esta función hace que este sea el método principal, donde iniciará el programa.      

# Menú de opciones en dónde el usuario elegirá que función desea hacer efectiva.

    while True: # Esta estructura nos permite regresar el menú cada vez que el usuario termine de utilizar una funcionalidad.

        print(" ======================================//====================================== \n")
        print("¡Bienvenido!\n")
        print("\nSeleccione una de las siguientes opciones:\n")
        print("1. Agregar una nota individual.\n2. Calcular promedio de notas.")
        print("3. Comparar notas según una nota de referencia.\n4. Consultar la notas de la lista guardada.")
        print("5. Salir\n")

        opcion_menu1 =input("Por favor digite la opción que desea elegir aquí: ---> ")
        if opcion_menu1=="1":
            continuar=True
            while continuar: #Esta sentencia hace que el usuario pueda reutilizar esta función sin necesidad de salir al menú inicial.
                
                print("Has elegido: Agregar una nota.")
                agregar_nota()

                while True:

                    opcion1=input("¿Desea seguir agregando notas?(S/N)").lower()

                    if opcion1=="n":
                        continuar=False
                        break

                    elif opcion1=="s":
                        continue

                    else:
                        print("Opción no válida, intente nuevamente")


        elif opcion_menu1=="2":
            print("Has elegido: Calcular promedio de notas.")
            calcular_promedio()

        elif opcion_menu1=="3":
            print("Has elegido: Comparar notas según una nota de referencia.")
            comparar_notas()

        elif opcion_menu1=="4":
            print("Has elegido: Consultar la existencia de una nota")
            consultar_nota()

        elif opcion_menu1=="5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intente nuevamente")

if __name__ == '__main__':
    main()


