def main():
    reports = 0
    with open('input2.txt') as f:
        for line in f:
            if line:
                values = line.strip().split()
                print('values: ', values)
                verified = verify_list(values)
                if verified: reports += 1

                print(f"The total right reports are : {reports}")


def verify_list(values):
    variation = None
    if len(values) < 2:
        return False

    for i in range(1, len(values)):
        gap = abs(int(values[i]) - int(values[i - 1]))
        print(f'This is ce gap between {values[i]} et {values[i - 1]} : {gap}')

        if gap < 1 or gap > 3: return False
        if int(values[i]) > int(values[i - 1]):
            if variation is None:
                variation = True
                print('est ce que ca monte ? ', variation)
            elif variation is False:
                return False
        elif int(values[i]) < int(values[i - 1]):
            if variation is None:
                variation = False
                print('est ce que ca descend ? ', variation)
            elif variation is True:
                return False
    return True


main()
