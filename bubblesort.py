def bubble_sort(angka):
    n = len(angka)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if angka[j] > angka[j + 1]:
                angka[j], angka[j + 1] = angka[j + 1], angka[j]
                swapped = True
        if not swapped:
            break
    return angka

angka = [2, 3, 1, 4, 5]
print("Contoh output:", bubble_sort(angka))  
