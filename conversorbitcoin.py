#Input del usuario
pesoscol = input("¿Cuantos pesos colombianos tienes ?")
pesoscol = float(pesoscol)
#Declaracion de valores
valor_dolar = 3679
valor_euro = 4383
valor_cake = 58800
valor_btc = 136134100
#Calculo valor dolar
dolares= pesoscol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
#Calculo Valor Euro
euros= pesoscol / valor_euro
euros = round(euros, 2)
euros = str(euros)
#Calculo Cantidad de CAKE
cakes = pesoscol / valor_cake
cakes = round(cakes, 4)
cakes = str(cakes)
#Calculo Bitcoin
btcs = pesoscol / valor_btc
btcs = round(btcs, 9)
btcs = str(btcs)
#Prints
print("Tienes $"+ dolares + " dolares")
print("Tienes $"+ euros + " Euros")
print("Tienes: " + cakes + " CAKE")
print("Tienes: " + btcs + " Bitcoins")