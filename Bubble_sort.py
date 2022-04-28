"""
Bubble sort

fetch last element in each step

[5,1,8,2]

stage 1 -

step 1: compare index 0 and 1 .if i[0]>i[1] then swap else remain same
[1,5,8,2]

step 2: compare index 1 and 2 .if i[1]>i[2] then swap else remain same
[1,5,8,2]

step 3: compare index 2 and 3 .if i[2]>i[3] then swap else remain same
[1,5,2,8]

stage 1 Result : [1,5,2,8] - placed the largest element at the end.
stage 2 Result : [1,2,5,8] - placed the second-largest element at the correct position
stage 3 Result : [1,5,2,8] - placed the third-largest element at the correct position

"""
"""
using 2 four loops:

efficiency :
TIME COMPLEXITY - O(n^2) SPACE COMPLEXITY - O(n)

how can we improve?
1. limit the range of for loop after each k iteration
2. if swapping not done in any i iterations then , no need to continue the iteration
because it is all sorted
"""


def bubble(data):

    for k in range(len(data)-1):
        swap = False
        for i in range(len(data)-1-k):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swap = True
        print(swap, data)
        if not swap:
            print("entered")
            return data

    return data


if __name__ == "__main__":
    data = [1,4,3,9,10]
    print(bubble(data))

# --------------------------------- exercise ------------------------------------------------------#

"""

Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

bubble_sort(elements, key='transaction_amount')
This will sort elements by transaction_amount and your sorted list will look like,

elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
But if you call it like this,

bubble_sort(elements, key='name')
output will be,

elements = [
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]

"""


def bubble(data, key):

    for k in range(len(data)-1):
        swap = False
        for i in range(len(data)-1-k):
            if data[i][key] > data[i+1][key]:
                data[i], data[i+1]= data[i+1], data[i]
                swap = True
        if not swap:
            return data

    return data


if __name__ == "__main__":
    elements = [
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
    print(bubble(elements,"name"))
    print(bubble(elements,'transaction_amount'))
