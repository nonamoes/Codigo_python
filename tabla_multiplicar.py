def run():
    tabla = int(input("Que tabla desea estudiar hoy?: "))
    limite = tabla * 10 +1
    a = tabla
    b = 0
    multi = a * b
    while multi < limite:
        print(str(a) + " x " + str(b) + " = " + str(multi))
        a = tabla
        b = b +1
        multi = a * b

if __name__ == "__main__":
    run()