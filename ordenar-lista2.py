#Ordenar lista

#Ya no entiendo este algoritmo :(
yn=input("¿Quieres ordenar la lista? Y/N:")
if yn.upper()=='Y':
    for k in range(4):
        for x in range(4):
            if lista[x]>lista[x+1]:
                aux=lista[x]
                lista[x]=lista[x+1]
                lista[x+1]=aux
    print("Lista ordenada: ")

print(lista)