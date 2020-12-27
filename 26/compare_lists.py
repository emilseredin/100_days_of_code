def parse_file(filename):
    numbers = []
    with open(filename) as f:
        numbers = [int(num) for num in f.readlines()]
    return sorted(numbers)


def compare_lists(list_1, list_2):
    intersection = [num for num in list_1 if num in list_2]
    return intersection


def main():
    list_1 = parse_file("./files/file_1.txt")
    list_2 = parse_file("./files/file_2.txt")
    intersection = compare_lists(list_1, list_2)
    print(intersection)


if __name__ == "__main__":
    main()
