def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("sorted_list:", sorted_list)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

target = 22
result = binary_search(sorted_list, target)
if result != -1:
    print(f"item {target} found on index  {result}.")
else:
    print(f"item {target} not found in the list. " )


def binary_search(A, Val):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1
    while First <= Last:
        Middle = (First + Last) // 2
        if value == A[Middle]:
            ResultOk = True
            Pos = Middle
            break
        elif Val > A[Middle]:
              First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print("Item found")
        return Pos
    else:
        print("Item  not found")
        return -1