# Создание кода для реализации алгоритма пузырьковой сортировки.

mas = [5, 7, 4, 3, 8, 2]
n = len(mas)

for run in range(n-1):
    for i in range(n-1-run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)

# Результат: [2, 3, 4, 5, 7, 8]