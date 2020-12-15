def count_expression_powers(expression, number):
    expression_powers = ['1']
    number_digits_amount = 0
    i = 1
    while len(expression) >= number_digits_amount:
        number_in_power = int(number) ** i
        binary_number = bin(int(number_in_power))[2:]
        number_digits_amount = len(binary_number)
        expression_powers.append(binary_number)
        i += 1
    expression_powers.pop()
    return expression_powers


def count_min_slices(expression, number):
    expression_powers = count_expression_powers(expression, number)
    slices = []
    while True:
        memoization_list = []

        for i in range(len(expression) + 1):
            if expression[:i] in expression_powers and expression[0] != '0':
                memoization_list.append(expression[:i])

        if len(memoization_list) == 0:
            return -1

        slices.append(memoization_list[-1])
        numbers_to_slice = len(memoization_list[-1])
        expression = expression[numbers_to_slice:]

        if expression == '':
            return len(slices)
