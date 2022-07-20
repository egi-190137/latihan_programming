# def cekEkstraKeju(angka):
#     temp = angka
#     arr = []
#     while temp > 0:
#         arr.insert(0, temp%10)
#         temp //= 10

#     total = 1
#     for item in arr:
#         total *= item
    
#     for item in arr:
#         total += item
    
#     return total==angka


n = int(input())

# total = 0
# for i in range(1, n+1):
#     if cekEkstraKeju(i):
#         total += 1
i = 1
while (i*9) + (i+9) < n and i < 10:
    i += 1 

print(i-1)