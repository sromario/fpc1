def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2 ] #escolhe pivo, elemento do meio
    left = [x for x in arr if x < pivot ] #elementos menores que pivot
    middle = [x for x in arr if x == pivot] #elementos iguais ao pivot
    right = [x for x in arr if x > pivot] #elementos maiores que pivot

    return quicksort(left) + middle + quicksort(right)

#entrada
arr = list(map(int,input().split()))

#ordenação
ordenada =quicksort(arr)

#impressão
print(ordenada)