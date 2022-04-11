"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

# а) итератор, генерирующий целые числа, начиная с указанного,

from itertools import count
from itertools import cycle

list_int = []

a = int(input("Введите первое число: "))
n = int(input("Введите последнее число: "))

for x in count(a):
    if x > n:
        break
    print(x)
    list_int.append(x)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
print()
print(list_int)

count = 0
for item in cycle(list_int):
    if count >= len(list_int):
        break
    print(item)
    count += 1
