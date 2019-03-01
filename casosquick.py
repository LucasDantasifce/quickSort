from random import randint, shuffle
import matplotlib as mpl
import timeit


Dlista = [10000, 20000, 30000, 40000, 50000]

def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,tam))
    shuffle(lista)

    return lista

def partition(list, n, start, end):
    list[start], list[n] = list[n], list[start]
    pivot = list[n]
    i = start + 1
    j = end
    while i <= j:
        while i <= j and list[i] < pivot:
            i += 1
        while list[j] > pivot:
            j -= 1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
    list[j], list[start] = list[start], list[j]
    return j

def quicksort(list, start, end):
    if end - start <= 1:
        return list
    j = partition(list, randint(start, end-1), start, end-1)
    quicksort(list, start, j)
    quicksort(list, j+1, end)
    return list


mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,ym, label = "Medio Tempo")
    ax.plot(x,yp, label = "Pior Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoCasos.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(melhor, reverse=True)

    MelhorCaso.append(timeit.timeit("aux={}\nquicksort(aux,0,len(aux))".format(melhor.copy()),setup="from __main__ import quicksort",number=1))
    PiorCaso.append(timeit.timeit("aux={}\nquicksort(aux,0,len(aux))".format(pior.copy()),setup="from __main__ import quicksort",number=1))
    MedioCaso.append(timeit.timeit("aux={}\nquicksort(aux,0,len(aux))".format(medio.copy()),setup="from __main__ import quicksort",number=1))



desenhaGrafico(Dlista,MedioCaso,MelhorCaso,PiorCaso)

