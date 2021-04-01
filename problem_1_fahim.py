import time


def make_list(f):
    l = []
    fi = open("{}.txt".format(f))
    my_fi = fi.read()
    l = my_fi.split(" ")
    l.pop()
    for i in range(len(l)):
        l[i] = int(l[i])
    return l


def bubble_sort(arr):
    n = len(arr)
    swapFlag = False
    start = time.time()

    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapFlag = True

        if swapFlag == False:
            break

    print(time.time() - start)
    print(arr)

    if len(arr)%2==0:
        median = (arr[int((n/2))] + arr[int((n/2-1))]) / 2
        print("Min:", arr[0], " Median:", median, " Max:", arr[n-1])
    else:
        print(arr[int(n/2)])
    print()


def insertion_sort(arr):
    start = time.time()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(time.time() - start)


def selection_sort(arr):
    start = time.time()

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(time.time() - start)


arr =  make_list("25 students")
arr2 = make_list("100 students")
arr3 = make_list("1000 students")
arr4 = make_list("10 000 students")

# bubble_sort(arr)
# bubble_sort(arr2)
# bubble_sort(arr3)
# bubble_sort(arr4)

# insertion_sort(arr)
# insertion_sort(arr2)
# insertion_sort(arr3)
# insertion_sort(arr4)

selection_sort(arr)
selection_sort(arr2)
selection_sort(arr3)
selection_sort(arr4)
