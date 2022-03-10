## CICLO WHILE
# def run():
#     tabla = int(input("Que tabla desea estudiar hoy?: "))
#     limite = tabla * 10 +1
#     a = tabla
#     b = 0
#     multi = a * b
#     while multi < limite:
#         print(str(a) + " x " + str(b) + " = " + str(multi))
#         a = tabla
#         b = b +1
#         multi = a * b

# if __name__ == "__main__":
#     run()



## Ciclo IF
# def run():
#     menu = ''' 
#     ----------------------------------
#     | Programa de Multiplicacion      |
#     | Escoge una tabla de multiplicar |
#     ----------------------------------

#     1-
#     2-
#     3-
#     4-
#     5-
#     6-
#     7-
#     8-
#     9- 
        
#     Escoge una opcion: '''

#     contador = 0
#     tabla = int(input(menu))
#     resultado = 0

#     if tabla == 0:
#         print(""" 
#         -------------------------------------
#         |!!! ELIGE UN NUMERO ENTRE 1 y 9 !!!|
#         -------------------------------------
#         """)
#     elif tabla  <= 9:
#         for contador in range(11):
#             print(str(tabla) + " por " + str(contador) + ' es igual a: ' + str(resultado))
#             contador += 1
#             resultado = tabla * contador
#     else:
#         print(""" 
#         -------------------------------------
#         |!!! ELIGE UN NUMERO ENTRE 1 y 9 !!!|
#         -------------------------------------
#         """) 

# if __name__ == "__main__":
#     run()


## Ciclo FOR
def run():
     print("Hola este es un programa que te da las tablas de multiplicar del numero que tu quieras")
     tabla = int(input("Que numero quieres multiplicar: "))
     for i in range(1,11):
         print("El resultado de " + str(tabla) + " por " + str(i) + " es igual a " + str(i*tabla))

if __name__ == "__main__":
     run()