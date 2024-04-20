from functools import reduce

def jumlah_kuadrat(angka):
    kuadrat = map(lambda x: x ** 2, filter(lambda x: x > 0, angka))
    total = reduce(lambda x, y: x + y, kuadrat, 0)
    return total

angka = [1, 2, 3, 4, 5]
print("Contoh output:", jumlah_kuadrat(angka)) 
