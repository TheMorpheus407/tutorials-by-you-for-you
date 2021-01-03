import random

"""
https://stanford.edu/~rezab/classes/cme323/S16/projects_reports/he.pdf
https://stackoverflow.com/questions/463105/in-place-radix-sort
vp
 #define bitsword 32   
 # #define bitsbyte 8    
 # #define bytesword 4  
 # #define R (1 << bitsbyte)  
 # #define digit(A, B)     
 # ((A >> (bitsword-(B+1)*bitsbyte)) & (R-1))

quicksortB(int a[], int l, int r, int w)  { 
    int i = l, j = r;    
    if (r <= l || w > bitsword) return;    
    while (j != i)    {      
         while (digit(a[i], w) == 0 && (i < j)) i++;      
         while (digit(a[j], w) == 1 && (j > i)) j--;      
         exch(a[i], a[j]);    
    }    
    if (digit(a[r], w) == 0) j++;    
    quicksortB(a, l, j-1, w+1);    
    quicksortB(a, j, r, w+1);  
}"""

def radix_msb_sort(unsorted_list: list, i: int, r: int, w: int) -> list:
    pass

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


"""
quicksortB(int a[], int l, int r, int w)  { 
    int i = l, j = r;    
    if (r <= l || w > bitsword) return;    
    while (j != i)    {      
         while (digit(a[i], w) == 0 && (i < j)) i++;      
         while (digit(a[j], w) == 1 && (j > i)) j--;      
         exch(a[i], a[j]);    
    }    
    if (digit(a[r], w) == 0) j++;    
    quicksortB(a, l, j-1, w+1);    
    quicksortB(a, j, r, w+1);  
}


def msdRadixSort(self, a, c = 0):
    # S2
    # MSD radix sort
    # T: O(dn), S: O(dn)
    """
    :type a: array
    :type c: current digit from left, start at 0
    """
    digits = lambda x: math.ceil(math.log(x + 1, 10))

    if c >= digits(max(a)) if a else 0:
        return a

    buckets = [[] for i in range(10)]

    for x in a:
        i = digits(x) - c
        idx = x % 10**i // 10**(i - 1) if i > 0 else 0
        buckets[idx].append(x)

    for i, b in enumerate(buckets):
        if len(b) > 1 and c + 1 < digits(max(b)):
            buckets[i] = self.msdRadixSort(b, c + 1)

    return functools.reduce(lambda x, y: x + y, buckets, [])

def lexicalOrder(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    x = list(range(1, n + 1))
    return self.msdRadixSort(x)"""