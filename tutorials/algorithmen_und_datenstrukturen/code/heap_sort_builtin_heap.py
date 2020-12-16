import random

from heapq import heappush, heappop


def heap_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    heap = []
    for item in unsorted_list:
        heappush(heap, item)
    return [heappop(heap) for _ in range(len(heap))]


def main() -> None:
    l = [random.randint(0, 999) for _ in range(9999)]
    print(heap_sort(l))


if __name__ == "__main__":
    main()
