import time
import random

def listaAleatorios():
    print("Ingrese cuantos numeros aleatorios desea obtener:")
    n = int(input())
    lista= []
    for i in range(n):
        lista.append(random.randint(1, 10000))
    return lista

def bubbleSort(arr):
    time_ini=time.time()
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    time_fin=time.time()
    time_dif=time_fin-time_ini
    return arr,time_dif

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    time_ini = time.time()
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    time_fin = time.time()
    time_dif = time_fin - time_ini
    # Driver code to test above
    return arr,time_dif

def main():
    arreglo=listaAleatorios()
    print("El arreglo a ordenar es: {} ".format(arreglo))
    ordenamiento_bubble,time_bubble=bubbleSort(arreglo)
    ordenamiento_insertion,time_insertion=insertionSort(arreglo)
    print("El arreglo ordenado por bubblesort es: {}".format(ordenamiento_bubble))
    print("El tiempo_bubble es : {}".format(time_bubble))
    print("El arreglo ordenado por insertion sort es: {} ".format(ordenamiento_insertion))
    print("El tiempo_insertion es : {}".format(time_insertion))
if __name__=='__main__':
    main()
