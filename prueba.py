#Ordenando una lista
n=int(input("Ingresa la cantidad de números: "))
i=0
lista=[]
while i<n:
    x=float(input("Ingresa número: "))
    lista.append(x)
    
    if i>0:
        if lista[i-1]<lista[i]:
            print("Vas en Ascendente")

        else:
            print("Ahora en Descendente")
    i+=1

#Ahora ordenamos la lista 
#Podrías hacerlo con sorted()
a=sorted(lista,reverse=True)
print(a)#lista ordenada en forma descendente
#pero si quieres ver como se haría de otra forma sería esta
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

else:
    print(lista)
