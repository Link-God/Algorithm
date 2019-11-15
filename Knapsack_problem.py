from sys import stdin
from collections import OrderedDict


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


def get_answer(capacity: int, weight_and_price):
    weight = list(weight_and_price.keys())
    price = list(weight_and_price.values())
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
    weight_and_price = OrderedDict()
    for line in obj:
        if line == '\n':
            continue
        list_of_numbers = list(map(int, line.split()))
        if len(list_of_numbers) == 1:
            capacity = list_of_numbers[0]
        else:
            weight, price = list_of_numbers
            weight_and_price[weight] = price

    return capacity, weight_and_price


if __name__ == '__main__':
    W, weight_and_price_dict = handler()
    ans = get_answer(W, weight_and_price_dict)
    print(sum(list(weight_and_price_dict.keys())[x - 1] for x in ans),
          sum(list(weight_and_price_dict.values())[x - 1] for x in ans))
    print(*ans, sep='\n')
