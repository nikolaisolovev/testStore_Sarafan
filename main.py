"""
выводит n первых элементов последовательности 122333444455555…
(число повторяется столько раз, чему оно равно)
"""


n = int(input('Введите n: '))
v = []

for i in range(1, n+1):
    v += [str(i)] * i

print(" ".join(v[:n]))