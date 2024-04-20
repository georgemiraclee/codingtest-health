def binary_search(angka, target):
    low = 0
    high = len(angka) - 1

    while low <= high:
        mid = (low + high) // 2
        if angka[mid] == target:
            return mid
        elif angka[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

angka = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
print("Contoh output:", binary_search(angka, target)) 

target = 3
print("Contoh output:", binary_search(angka, target)) 
