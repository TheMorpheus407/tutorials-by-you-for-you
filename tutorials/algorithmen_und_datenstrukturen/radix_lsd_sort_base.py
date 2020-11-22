import random


def radix_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    _BASE = 10
    maximum = max(unsorted_list)

    factor = 1
    while factor <= maximum:
        partition = [[] for _ in range(_BASE)]
        for item in unsorted_list:
            partition[(item // factor) % _BASE] += [item]

        unsorted_list = []
        for segment in partition:
            unsorted_list += segment

        factor *= _BASE
    return unsorted_list


def main() -> None:
    l = [random.randint(0, 999) for _ in range(10)]
    print(radix_sort(l))


if __name__ == "__main__":
    main()
