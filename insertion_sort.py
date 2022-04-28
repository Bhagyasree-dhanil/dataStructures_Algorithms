"""
insertion sort

we can sort values  by insertion into another array in order
In INSERTION SORT instead of using another array, insert in the same element in order

for eg:

data= 6, 2, 5, 1

# initial condition
[6] 2,5,1 - data[0] is sorted array with one element within array

1.  if data[0] > data[1]  - then insert data[1] in index 0

now  we get sorted array of two elements within array
[2, 6],5,1

2. if data[2] < data[0]  - false
  if data[2] < data[1] - true  then insert data[2] in index 1

now  we get sorted array of three elements within array
[2, 5, 6],1

3. if data[3] < data[0]  -  true  then insert data[2] in index 0

now  we get fully sorted array
"""


def insertion_sort(data):

    for i in range(1, len(data)):
        for k in range(i):
            if data[i] < data[k]:
                data[k], data[i] = data[i], data[k]


def sort_by_insertion(data):

    for i in range(1, len(data)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


if __name__ == "__main__":

    elements = [8, 2, 5, 1]
    insertion_sort(elements)
    print(elements)

# -----------------------------------exercise -1 ----------------------------------------------------#

"""
find the running median of a sequence of no. Median of even is the average of two middle no in the sorted_list.
arr=[2, 1, 5, 7, 2, 0, 5]
"""


def sort_list(data):
    for i in range(1, len(data)):
        for k in range(i):
            if data[i] < data[k]:
                data[k], data[i] = data[i], data[k]
    return data


def list_median(arr) :

    cum_median=[]
    for i in range(len(arr)):
        data = sort_list(arr[0:i+1])
        len_data = len(data)
        var = int(len_data / 2)
        if i == 0:
            med = data[i]
        elif len_data % 2 == 0:
            # even
            med = (data[var] + data[var-1])/2
        else:
            med = data[var]
        cum_median.append(med)
        print(data, var, med)
    return cum_median


if __name__ == "__main__":
    arr = [2, 1, 5, 7, 2, 0, 5]
    print(list_median(arr))


