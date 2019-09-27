# http://fit.nsu.ru/data_/courses/niu/daio_komb_alg_uchpos.pdf

n = 4
a = [t for t in range(1, n + 1)]
i = 1
n -= 1  # для индексов
while i >= 0:
    print(a)
    i = n - 1
    while a[i] > a[i + 1]:
        i -= 1
    j = n
    while a[j] < a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    # print(a[i::])
    a[i + 1::] = a[i + 1::][::-1]
