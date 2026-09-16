arr = [1, 5, 2, 9, 3]


def sort_arr(arr):
    # write your code below
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# write main function to test your sort_arr
if __name__ == "__main__":
    print("排序前:", arr)
    result = sort_arr(arr)
    print("排序后:", result)
