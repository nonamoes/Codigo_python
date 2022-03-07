# Imprimir numeros pares unicamente 
from ast import Break


def run():
    
    #usando continue
    # for contador in range(1000):
    #     if contador %2 != 0:  
    #         continue
    #     print(contador)
    
    #usando break Se corta hasta donde indique
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    #usando break con un texto
    texto = input("Escribe un texto: ")        
    for letra in texto:
        if letra == "o": #si encuentra la letra o, se detendra
            break
        print(letra)

if __name__ == "__main__":
    run()