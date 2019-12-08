from sys import stdin
from math import gcd
from functools import reduce


def create_table(capacity: int, weight: list, price: list):
    matrix = [[0] * (capacity + 1) for _ in range(len(weight) + 1)]
    for quantity in range(1, len(weight) + 1):
        for cur_capacity in range(1, capacity + 1):
            if cur_capacity >= weight[quantity - 1]:
                matrix[quantity][cur_capacity] = max(matrix[quantity - 1][cur_capacity],
                                                     matrix[quantity - 1][cur_capacity - weight[quantity - 1]] + price[
                                                         quantity - 1])
            else:
                matrix[quantity][cur_capacity] = matrix[quantity - 1][cur_capacity]
    return matrix


def get_answer(capacity: int, weight_and_price: list):
    weight = [tup[0] for tup in weight_and_price]
    price = [tup[1] for tup in weight_and_price]
    # находим НОД для эффективности по памяти
    nod = reduce(gcd, [capacity] + weight)
    capacity = capacity // nod
    weight[:] = map(lambda x: x // nod, weight)
    matrix = create_table(capacity, weight, price)
    answer = list()

    def fill_answer(current_num_element, current_capacity):
        if matrix[current_num_element][current_capacity] == 0:
            return
        elif matrix[current_num_element - 1][current_capacity] == matrix[current_num_element][current_capacity]:
            fill_answer(current_num_element - 1, current_capacity)
        else:
            fill_answer(current_num_element - 1, current_capacity - weight[current_num_element - 1])
            answer.append(current_num_element)

    fill_answer(len(weight_and_price), capacity)

    return answer


def handler(obj=stdin):
    capacity = 0
    weight_and_price = list()
    for line in obj:
        if line == '\n':
            continue
        list_of_numbers = list(map(int, line.split()))
        if len(list_of_numbers) == 1:
            capacity = list_of_numbers[0]
        else:
            weight, price = list_of_numbers
            weight_and_price.append((weight, price))

    return capacity, weight_and_price


if __name__ == '__main__':
    W, weight_and_price_list = handler()
    ans = get_answer(W, weight_and_price_list)
    print(sum([tup[0] for tup in weight_and_price_list][x - 1] for x in ans),
          sum([tup[1] for tup in weight_and_price_list][x - 1] for x in ans))
    print(*ans, sep='\n')
