def run():
    mi_diccionario ={  #se utilizan las llaves ={} para crear diccionarios
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    
    poblacion_paises ={
        "Argentina" : 444938750,
        "Brasil" : 152222222,
        "Mexico" : 85222221,
    }

    #print(poblacion_paises["Argentina"])

    
    #recorrer el valoor de las llaves con ciclo for
    # for pais in poblacion_paises.keys(): #metodo de los diccionarios que nos devuelven las llaves
    #     print(pais)
    
    # for pais in poblacion_paises.values(): #metodo de los diccionarios que nos devuelven los valores
    #     print(pais)

    #quiero hacer un print que muestre los dos
    for pais, poblacion in poblacion_paises.items(): #metodo de los diccionarios que nos devuelven las llaves y el valor que es lo mismo de arriba
        print(pais +  " tiene " + str(poblacion) + " habitantes")

if __name__ == "__main__":
    run()