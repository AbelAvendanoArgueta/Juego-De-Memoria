#Baruc Fabián Velasquez Ruíz
#Abel Fernando Avendaño Argueta

        ##################
        #   Importaciones
        ##################
import random

        ##################
        #   Listas  y variables globales
        ##################

# Se requiere una terminal con capacidad de mostrar caracteres Unicode
# representa la cara de cada carta 
cartas = [
        '☺', '☺', '♦', '♦', '♥', '♥', '☼', '☼', '☻', '☻', '♫', '♫', '♣', '♣', '♠', '♠',
        '🤑','🤑', '🤨', '🤨', '😡', '😡', '😈', '😈', '💩', '💩', '🤡', '🤡', '👹', '👹', '👺', '👺',
        '👻', '👻', '👽', '👽', '👾', '👾', '🤖',  '🤖', '💌', '💌', '💘', '💘', '💔', '💔', '❤', '❤',
        '💙', '💙', '🤍', '🤍', '💦', '💦', '💥', '💥', '💨', '💨', '😦', '😦', '🖖', '🖖', '🖐', '🖐'
        ]
# representa si mostrar la cara de cada carta
mostrar = [False]*64 #####!!!!!###
# representa el número de coincidencias realizadas
pares_descubiertos = 0
# representa el número de vueltas tomadas
numero_de_intentos = 0

        ##################
        #Fin de Listas
        ##################
        #Funciones
        ##################


# imprime la pantalla de bienvenida y las instrucciones
def welcome():
    print('\nBienvenido al juego!')
    print('\nEste es un juego de memoria en el que adivinas dos cartas.')
    print('Si las caras de las cartas que eliges coinciden, ganas el par,')
    print('y quedan boca arriba.')
    input('\nIngrese cualquier número para CONTINUAR: ')

# imprime la lista de 'tarjetas' basada en la lista de 'mostrar'
def imprimir_cartas(cartas, mostrar):
    print()
    for index, carta in enumerate(cartas):
        # verificar si ocultar o mostrar cada carta usando la lista 'mostrar'
        if mostrar[index] == False:
            print('■', end=' ') # ocultar
        else:
            print(carta, end=' ') # mostrar
        # imprimir una nueva línea cada 8 tarjetas ##!!!!##
        if (index + 1) % 8 == 0: #####!!!!!###
            print() # nueva linea

# verificar si la seleccion de cartas es válida
def adivinando_carta(mostrar):
    adivinacion = 0 # variable numerica # int(input()) podria provocar un error
    while True:
        # Obtener una conjetura del usuario !!!explain
        adivinacion = input('\nAdivine una carta: ')
        # validar adivinanza, es la eleccion numerica?
        if adivinacion.isnumeric() == False:
            print('\nEntrada inválida. Inténtalo de nuevo.')
            continue
        # convertir string en un integer
        adivinacion = int(adivinacion)
        # comprobar: fuera de los límites
        if adivinacion < 1 or adivinacion > 64: #####!!!!!###
            print('\nEntrada inválida. Inténtalo de nuevo.')
            continue
        # decremento en 1 para fines de indexación de base cero
        adivinacion -= 1
        # verificación: "elegido" o "emparejado" o "seleccion previa", según la lista 'mostrar'
        if mostrar[adivinacion]:
            print('\nEntrada inválida. Inténtalo de nuevo.')
            continue
        # superó todas las comprobaciones, conjetura válida, selección valida
        # adivino correctamente
        return adivinacion

# hacer una pausa antes de comenzar el siguiente turno y permitir que el usuario salga o continúe jugando
def ligera_pausa():
    # Obtener entrada del usuario
    reply = input('\nIntroduzca 0 para SALIR. Ingrese cualquier otro caracter para CONTINUAR: ')
    # verificar si el usuario ingresó '0'
    if reply == '0':
        print('\n¡Gracias por jugar!\n')
        quit()

        ##################
        #Fin de Funciones
        ##################
        #Inicio de ejecución del programa
        ##################

welcome()

#Aleatorizar juego 
random.shuffle(cartas)

# el juego se repite hasta que se hayan completado todos los pares
while pares_descubiertos != 8:
    # imprime la lista de 'cartas' basada en la lista de 'mostrar'
    imprimir_cartas(cartas, mostrar)

    # obtener una conjetura de tarjeta válida del usuario
    adivinacion1 = adivinando_carta(mostrar)
    # actualice la lista 'mostrar' para mostrar la cara de la tarjeta cuando se imprima
    mostrar[adivinacion1] = True

    imprimir_cartas(cartas, mostrar)

    adivinacion2 = adivinando_carta(mostrar)
    mostrar[adivinacion2] = True

    imprimir_cartas(cartas, mostrar)

    # verificar si las cartas adivinadas son un par válido
    if cartas[adivinacion1] == cartas[adivinacion2]:
        print('\nCoincide! Par válido (っ ͡⚈ ᴗ ͡⚈)っ')
        # incrementar el número de coincidencias hechas
        pares_descubiertos += 1
    else:
        print('\nNo coincide. Par inválido (っ ͡⚈ ︹ ͡⚈)っ')
        # actualice la lista 'mostrar' para ocultar la cara de la tarjeta cuando se imprima
        mostrar[adivinacion1] = False
        mostrar[adivinacion2] = False

    # incrementar el número de vueltas tomadas
    numero_de_intentos += 1

    # comprobar si se han realizado todas las coincidencias, seleccionado todos los pares
    # esto es para evitar pausas después de ganar el juego
    if pares_descubiertos != 32: #####!!!!!###
        # hacer una pausa antes de comenzar el siguiente turno y permitir que el usuario salga o continúe jugando
        ligera_pausa()

else: # todos los pares han sido realizados
    # imprime la pantalla ganadora y el número de vueltas
    print('\n¡Felicidades! ¡Bien hecho! (っ ͡⚈ ω ͡⚈)っ')
    print('\nNúmero de intentos:', numero_de_intentos, '\n')