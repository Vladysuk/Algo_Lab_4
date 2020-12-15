from dynamic_approach import count_min_slices, count_number_powers, binary_to_int

if __name__ == "__main__":
    with open('fantz.in', 'r+') as fileIn:
        expression, number = fileIn.readline().split()

    with open('fantz.out', 'w+') as fileOut:
        fileOut.write("%d" % count_min_slices(expression, number))