def check_line(line):
    inc = [line[i + 1] - line[i] for i in range(len(line) - 1)]

    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


data = [[int(y) for y in x.split(' ')] for x in open('input2.txt').read().split('\n')]

safe_count = sum([check_line(line) for line in data])
print(safe_count)

safe_count = sum([any([check_line(line[:i] + line[i + 1:]) for i in range(len(line))]) for line in data])
print(safe_count)

