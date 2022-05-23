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

"""
Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

merge_sort(elements, key='time_hours', descending=True)
This will sort elements by time_hours and your sorted list will look like,

elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
But if you call it like this,

merge_sort(elements, key='name')
output will be,

elements = [
        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        ]
"""


def merge_sort(arr, key, descending):


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
    elements = [
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
    ]

    merge_sort(elements, key="name", descending=True)
    print(elements)