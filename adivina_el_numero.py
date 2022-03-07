#importaremos un modulo, en este caso el random
import random 


def run():
    numero_aleatorio = random.randint(1, 100)  #mandamo llamar al modulo y una funcion que tenga
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print ("Busca un número más grande")
        else:
            print("Busca un numero más pequeño")
        numero_elegido = int(input("Elige otro numero dentro del 1 al 100: "))
    print("Ganaste! :3")

if __name__ == "__main__":
    run()