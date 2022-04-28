"""
Merge sort



"""


def merge_sort(arr):

    if len(arr) <= 1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    sort_two_arrays(left, right, arr)


def sort_two_arrays(d1, d2, arr):

    d1_cnt = 0
    d2_cnt = 0
    k = 0

    while d1_cnt < len(d1) and d2_cnt < len(d2):
        if d1[d1_cnt] <= d2[d2_cnt]:
            arr[k] = d1[d1_cnt]
            d1_cnt += 1
        else:
            arr[k] = d2[d2_cnt]
            d2_cnt += 1
        k += 1

    while d1_cnt < len(d1):
        arr[k] = d1[d1_cnt]
        d1_cnt += 1
        k += 1

    while d2_cnt < len(d2):
        arr[k] = d2[d2_cnt]
        d2_cnt += 1
        k += 1


if __name__ == "__main__":
    arr = [10, 5, 2, 6]
    merge_sort(arr)
    print(arr)

# ==================================== Exercise ================================================================#

