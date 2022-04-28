"""
Quick sort

select a pivot element in data and move that to correct sorted position
that means,
before that pivot - datas will be lesser
after pivot  - datas will be greater.

The process of putting pivot into its position is called partitioning

Two type of partition schemes

1. Hoare partition

pivot - 0
start - 1
end - len(data)-1

(a) increment index of start until it get element > pivot
(b) decrement index of end until it get element < pivot

when 2 condition satisfies then swap
when start >end:  then swap pivot and end

2. Lomuto partition

pivot - len(data)-1
p_index - 0
end_index - len(data)

(a). increment p index until element > pivot
(b). now from p_index inc i_index until element < pivot

when 2 condition satisfies then swap
"""


def swap(a, b, data):
    if a == b:
        return
    else:
         data[a], data[b] = data[b], data[a]


def hoare_partition(data, start, end):
    pivot_index = start
    pivot = data[pivot_index]

    while start < end:

        while start < len(data) and data[start] <= pivot:
            start += 1

        while data[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, data)
        else:
            swap(pivot_index, end, data)
    return end


def lomuto_partition(data, start, end):

    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        p = p_index
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index +=1

    swap(p_index, end, elements)
    return p_index


def quick_sort(data, start, end):

    """
    if start < end:
        pa = hoare_partition(data, start, end)
        quick_sort(data, start, pa-1) # left partition
        quick_sort(data, pa+1, end) # end partition
    """

    if len(elements) == 1:
        return

    if start < end:
        pa = lomuto_partition(data, start, end)
        quick_sort(data, start, pa - 1)  # left partition
        quick_sort(data, pa + 1, end)  # end partition


if __name__ == "__main__":
    elements = [11, 9, 25, 7, 2, 15]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

