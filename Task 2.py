def my_sort(l):
    n = len(l)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if l[j] > l[j + 1]:
                swapped = True
                l[j], l[j + 1] = l[j + 1], l[j]

        if not swapped:
            return l

    return l

if __name__ == "__main__":
    l = [int(c) for c in input().split()]
    sorted = my_sort(l)
    print(sorted)

