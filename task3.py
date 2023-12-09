n_str = input('Введите число строк: ')
width = 0
for _ in range(len(n_str)):
    width += 1
n = int(n_str)
string = str(1).center(width)
result = []
for i in range(1, n+1):
    result.append(string)
    string = str(i+1).center(width) + string + str(i + 1).center(width)
max_width = len(result[-1])
for row in result:
    print(row.center(max_width))
