# [9, 10, 2, 5, 7]
# [10, 2, 5 ,7 ,9]
a = input('Введите элементы списка через пробел: ').split()
a = list(map(int, a))
move = int(input('Введите число сдвигов элементов списка: '))
if move < 0:
    for i in range(abs(move)):
        a.insert(0, a[-1])
        del a[-1]

for i in range(move):
    a.append(a[0])
    a.remove(a[0])

print(a)