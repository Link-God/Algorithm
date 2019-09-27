def prime(n):
    for j in range(2, int(n ** (1 / 2)) + 1):
        if n % j == 0:
            return False
    return True

# test
