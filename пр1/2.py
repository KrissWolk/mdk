a = int(input())
suma = 0

while a > 0:
    suma = suma + a % 10
    a = a // 10

print(suma)
