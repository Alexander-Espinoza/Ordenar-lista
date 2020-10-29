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
            print("Vas en Descendente")
    i+=1

print(lista)
#Ahora ordenamos la lista 
#Podrías hacerlo con sorted()
a=sorted(lista,reverse=True)
print(a)#lista ordenada en forma descendente