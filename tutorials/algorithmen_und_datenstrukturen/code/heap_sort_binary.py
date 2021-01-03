import random


def heapify(heap: list, n: int, i: int) -> list:
    max_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[max_index] < heap[left]:
        max_index = left

    if right < n and heap[max_index] < heap[right]:
        max_index = right

    if max_index != i:
        heap[i], heap[max_index] = heap[max_index], heap[i]
        heap = heapify(heap, n, max_index)

    return heap


def heap_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    n = len(unsorted_list)

    for i in reversed(range(n//2)):
        unsorted_list = heapify(unsorted_list, n, i)

    for i in reversed(range(1, n)):
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        unsorted_list = heapify(unsorted_list, i, 0)
    
    return unsorted_list


def main() -> None:
    l = [random.randint(0, 999) for _ in range(9999)]
    print(heap_sort(l))


if __name__ == "__main__":
    main()
