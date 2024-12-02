list1 = []
list2 = []


def main():
    parse_input('./input.txt')


def parse_input(input_file):
    global list1, list2

    with open(input_file) as f:
        for line in f:
            if line:
                values = line.strip().split(maxsplit=1)
                # print('values: ', values)
                list1.append(int(values[0]))
                list2.append(int(values[1]))

        list1.sort()
        list2.sort()

        gap_list = [abs(a - b) for a, b in zip(list1, list2)]
        print('The total distance between lists : ', sum(gap_list))

        results_list = multiply_per_occurence(list1, list2)
        print('The sum of similarity is: ', sum(results_list))


def multiply_per_occurence(list1, list2):
    results = []

    for elem in list1:
        count = list2.count(elem)
        if count > 0:
            results.append(int(elem) * count)

    return results


main()
