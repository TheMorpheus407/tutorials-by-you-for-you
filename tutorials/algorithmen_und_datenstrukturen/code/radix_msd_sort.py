import random
    

def radix_msb_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    base = max(unsorted_list).bit_length() - 1

    return sort(unsorted_list, 0, len(unsorted_list) - 1, base)


def sort(unsorted_list: list, i: int, j: int, base: int) -> list:
    m, n = i, j
    while m <= n:
        if (unsorted_list[m] >> base) & 1 == 0:
            m += 1
            continue

        if (unsorted_list[n] >> base) & 1 == 0:
            unsorted_list[n], unsorted_list[m] = unsorted_list[m], unsorted_list[n]
            m += 1
        n -= 1

    if base > 0 and i < j:
        sort(unsorted_list, i, m - 1, base - 1)
        sort(unsorted_list, m, j, base - 1)

    return unsorted_list


def main() -> None:
    l = [random.randint(0, 999) for _ in range(9999)]
    print(radix_msb_sort(l))


if __name__ == "__main__":
    main()
