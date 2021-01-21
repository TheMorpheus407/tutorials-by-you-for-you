import random
    

def radix_msb_sort(unsorted_list: list, base=None) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    if base is None:
        base = max(unsorted_list).bit_length() - 1

    if base < 0:
        return unsorted_list

    m, n = 0, len(unsorted_list) - 1
    while m <= n:
        if (unsorted_list[m] >> base) & 1 == 0:
            m += 1
            continue

        if (unsorted_list[n] >> base) & 1 == 0:
            unsorted_list[n], unsorted_list[m] = unsorted_list[m], unsorted_list[n]
            m += 1
        n -= 1
        

    return [
        *radix_msb_sort(unsorted_list[:m], base - 1),
        *radix_msb_sort(unsorted_list[m:], base - 1)
    ]


def main() -> None:
    l = [random.randint(0, 999) for _ in range(9999)]
    print(radix_msb_sort(l))


if __name__ == "__main__":
    main()
