import random


_BASE = 10


def counting_sort(unsorted_list: list, factor) -> list:
    output = [0] * len(unsorted_list)
    count = [0] * _BASE
  
    for item in unsorted_list:
        count[(item // factor) % _BASE] += 1
  
    for i in range(1, _BASE): 
        count[i] += count[i - 1] 
    
    for item in reversed(unsorted_list):
        index = (item // factor) % _BASE
        output[count[index] - 1] = item
        count[index] -= 1  

    return output


def radix_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    maximum = max(unsorted_list)

    factor = 1
    while factor <= maximum:
        unsorted_list = counting_sort(unsorted_list, factor)
        factor *= _BASE

    return unsorted_list


def main() -> None:
    l = [random.randint(0, 999) for _ in range(9999)]
    print(radix_sort(l))


if __name__ == "__main__":
    main()
