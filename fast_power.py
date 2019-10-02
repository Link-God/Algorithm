def power(a, n):
    result = 1
    a_in_power = a
    while int(n) > 0:
        if n % 2:
            result *= a_in_power
        a_in_power *= a_in_power
        n = n >> 1
    return result


print(power(3, 5))

# test master
