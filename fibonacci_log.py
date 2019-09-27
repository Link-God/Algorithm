from pprint import pprint
from copy import deepcopy


def multiply_matrix(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def power_matrix(M, power):
    # if power == 1:
    #     return M
    # if power % 2 == 0:
    #     B = power(M, power / 2)
    #     B = multiply_matrix(B, B)
    #     return B
    # else:
    #     B = power(M, (power - 1) / 2)
    #     B = multiply_matrix(B, B)
    #     B = multiply_matrix(B, M)
    # return B

    result = [[1 if i == j else 0 for i in range(len(M[0]))] for j in range(len(M))]
    M_in_power = deepcopy(M)
    while int(power) > 0:
        if power % 2:
            result = multiply_matrix(result, M_in_power)
        M_in_power = multiply_matrix(M_in_power, M_in_power)
        power = power >> 1
    return result


X = [[1, 1],
     [1, 0]]

n = 0
# if fibonacci is : 1 1 2 ...
# iterate start with 0
print(power_matrix(X, n)[0][0])
