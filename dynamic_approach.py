def binary_to_int(expression):
    expression = expression[::-1]
    sum = 0
    for i in range(len(expression)):
        sum += int(expression[i]) * 2 ** i
    return sum


def count_number_powers(expression, number):
    number_powers = [1]
    number_digits_amount = 0
    i = 1
    while len(expression) >= number_digits_amount:
        number_in_power = int(number) ** i
        binary_number = bin(int(number_in_power))[2:]
        number_digits_amount = len(binary_number)
        number_powers.append(number_in_power)
        i += 1
    number_powers.pop()

    return number_powers


def count_min_slices(expression, number):
    number_powers = count_number_powers(expression, number)
    slices = []
    while True:
        memoization_list = []

        for i in range(len(expression) + 1):
            if binary_to_int(expression[:i]) in number_powers and expression[0] != '0':
                memoization_list.append(expression[:i])

        if len(memoization_list) == 0:
            return -1

        slices.append(memoization_list[-1])
        numbers_to_slice = len(memoization_list[-1])
        expression = expression[numbers_to_slice:]

        if expression == '':
            return len(slices)