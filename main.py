import numpy
from matplotlib import pyplot as plt

massiv_fibo = []
x = []

def fibonachy(n):
    if n == 1 or n == 2:
        return 1
    return fibonachy(n - 1) + fibonachy(n - 2)

for i in range(1, 10):
    massiv_fibo.append(fibonachy(i))
    x.append(i)

plt.plot(x, massiv_fibo, color='red', marker='o', markersize=7)
plt.xlabel('Номер Фибоначчи')
plt.ylabel('Величина числа Фибоначчи')
plt.show()
print(massiv_fibo)