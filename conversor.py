pesos = input("¿Cuántos pesos mxn tienes?: ")
pesos = float(pesos)
valor_dolar = 20.95
dolares= pesos / valor_dolar 
dolares = round(dolares, 2) 
dolares = str(dolares)
print("Tienes $" + dolares+ " dólares.")
