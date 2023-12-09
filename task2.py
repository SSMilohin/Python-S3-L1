n_str = input('Введите число строк: ')
width = 0
for _ in range(len(n_str)):
    width += 1
n = int(n_str)

print('С помощью чисел:')
for i in range(1, n + 1):
    for j in range(1, i + 1):
        difference = width - len(str(j))
        if difference != 0:
            print(j, ' '*difference, sep='', end='')
        else:
            print(j, end='')
    print()
print()

print('С помощью строк:')
string = str(1).ljust(width)
for i in range(1, n+1):
    print(string)
    string += str(i+1).ljust(width)
