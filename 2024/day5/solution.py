import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        rules_list = []
        orders_list = []
        switch = False

        for line in file:

            if line == '\n':
                switch = True
                continue

            if not switch:
                rule = line.split('|')
                rule = [int(number) for number in rule]
                rules_list.append(rule)

            else:
                order = line.split(',')
                order = [int(number) for number in order]
                orders_list.append(order)

    rules = np.array(rules_list)

    return rules, orders_list


def check_orders(rules, orders):

    good_orders = []
    bad_orders = []

    for order in orders:

        wrong = False

        for i in range(len(order) - 1):

            indices = np.where(rules[:, 1] == order[i])[0]

            for number in order[i + 1:]:

                if number in rules[indices, 0]:

                    wrong = True

        if not wrong:
            good_orders.append(order)
        else:
            bad_orders.append(order)

    return good_orders, bad_orders


def fix_orders(rules, orders):

    fixed_orders = []

    for order in orders:

        fixed_order = order.copy()
        i = 0

        while i < len(order) - 1:

            indices = np.where(rules[:, 1] == order[i])[0]
            leaders = rules[indices, 0]

            for j in range(len(order[i + 1:])):

                if order[i + 1 + j] in leaders:
                    fixed_order[i] = order[i + 1 + j]
                    fixed_order[i + 1 + j] = order[i]
                    order = fixed_order.copy()
                    i -= 1
                    break

            i += 1

        fixed_orders.append(fixed_order)

    return fixed_orders


def sum_middle_numbers(orders):

    middle_numbers = []

    for order in orders:

        middle_numbers.append(order[len(order) // 2])

    sum = np.sum(middle_numbers)

    return sum


def main():

    file_path = '2024/day5/input.txt'

    rules, orders = parse_input_file(file_path)

    good_orders, bad_orders = check_orders(rules, orders)

    fixed_orders = fix_orders(rules, bad_orders)

    good_sum = sum_middle_numbers(good_orders)
    fixed_sum = sum_middle_numbers(fixed_orders)

    print("The sum of the middle numbers of gthe good orders is", good_sum)
    print("The sum of the middle numbers of the fixed orders is", fixed_sum)


if __name__ == '__main__':
    main()
