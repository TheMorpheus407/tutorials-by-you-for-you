import random


def radix_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    bit_length = max(unsorted_list).bit_length()

    for bit in range(bit_length):
        partition = [[], []]
        for item in unsorted_list:
            partition[(item >> bit) & 1] += [item]

        unsorted_list = [*partition[0], *partition[1]]

    return unsorted_list


def main() -> None:
    l = [random.randint(0, 999) for _ in range(9999)]
    print(radix_sort(l))


if __name__ == "__main__":
    main()
