import re


def search_mul(file):
    final_result = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(file, 'r') as f:
        text = f.read()

    result_regex = re.findall(pattern, text)
    # print(result_regex)
    for obj in result_regex:
        result = int(obj[0]) * int(obj[1])
        final_result += result
        # print(final_result)


def search_mul_do_and_dont(file):
    pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    final_result = 0
    ignore = False

    with open(file, 'r') as f:
        text = f.read()

    result_regex = re.findall(pattern, text)
    # print(result_regex)
    for obj in result_regex:
        # print(f" obj to check : {obj}, ignore it ? {ignore}")
        if ignore:
            if obj == "do()":
                ignore = False
        else:
            if obj == "don't()":
                ignore = True

            elif obj.startswith("mul"):
                match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", obj)
                if match:
                    x = int(match.group(1))
                    y = int(match.group(2))
                    result = (x * y)

                    final_result += result
        # print(final_result)


search_mul('input3.txt')
search_mul_do_and_dont('input3.txt')
