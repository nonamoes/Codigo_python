import random

def generar_contrasena():
    mayusc = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusc = [ "a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbolos = ["!", "@","#", "$", "%", "&", "/", "(", ")", "*", "-", ".", ";"]
    numeros = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

    caracteres = mayusc + minusc + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    #si pongo las comillas simples ' ' generamos un string de la lista original
    contrasena = ''.join(contrasena) 
    return contrasena

def run():
   contrasena = generar_contrasena()
   print("Tu nueva contraseña es: " + contrasena)


if __name__ == "__main__":
    run()