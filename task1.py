n = input('Введите 3 числа(через пробел): ').split()
n1, n2, n3 = int(n[0]), int(n[1]), int(n[2])
result = 0
if n1 == n2:
    if n1 == n3:
        result = 3
    else:
        result = 2
else:
    if n1 == n3 or n2 == n3:
        result = 2
print(result)
