

# =============== what is list?================================================= #
"""

* list is used as a collection of heterogeneous data (different types of data- int, string, boolean etc)
* list items are ordered, mutable( changeable) and allow duplicate values
* list items are indexed.First item has index[0] and second one has index[1]

"""

# How to access elements in list using index:

list_arr = ['mango',2,5.7,True]

# index_order=[0,1,2,3] or [-4,-3,-2,-1]

data5 = list_arr[1]
data6 = list_arr[-3]

# accessing a part of list syntax= list[start:end:step]

data1 = list_arr[0:2:1] # end value is not included.
data2 = list_arr[-4:-2:1]

data3 = list_arr[4:]  # ==> 4 to last index
data4 = list_arr[:2]  # ==>  0 to 2 nd index


# reversing the list

rev_data = list_arr[::-1]

# check the element present or not

if "mango" in list_arr:
    pass

# change item_value

list_arr[0] = "banana"
list_arr[1:3] = [5, 10]


# insert items in a given index ==> list_arr.insert(index, data)
list_arr.insert(2, "orange")

# insert a value in the end of the list
list_arr.append("grapes")

# insert a new list  in the end of the list
list_arr.extend([3, 7, 8.9])


# remove a data ==> list.remove(data)

# list_arr.remove("mango")


# To remove a specified index ==> pop(index)

list_arr.pop(1)  # remove first index

list_arr.pop()  # remove last item


# delete using 'del' keyword

del list_arr[2]  # delete 2nd index item

# del list_arr  # delete the entire list
 
# list_arr.clear()  # to empty the list ,list without content

# sort list
list_arr=["mango", "carrot", "apple"]

list_arr.sort()   # ascending

list_arr.sort(reverse=True)   # descending

list_arr.sort(key=str.lower)  # case-insensitive sort

list_arr.reverse()  # will reverse the array

# copy of the list

newlist = list_arr.copy()
newlist2 = list(list_arr)

# joining two lists

list1=["a", "b", "c"]
list2=["mango", "orange"]

join_list = list1+list2

# or use extend

join_list2 = list1.extend(list2)

# return the first index of given value

# index_val=join_list.index("a")


# ================ 'code basics' - youtube tutorial on arrays =================#

# store apple's stock  price for 5 days

stock_price = [298, 305, 320, 301, 295]

# what was price on 2 nd day?

price_day2 = stock_price[1]
# print(price_day2)

'''
order of complexity of lookup by index is O(1)
time constant operation

'''

# on what day price is 301?

for i in range(len(stock_price)):
    if stock_price[i] == 301:
        day = i+1
        break

'''
order of complexity of finding index by data is O(n).
since we need to iterate over a array
as size increase ,time also increase

'''


# print all values in a array? - array traversal

for i in stock_price:
    data = i

'''
order of complexity of array traversal  is O(n).
since we need to iterate over a array
as size increase ,time also increase

'''

# insert a element in day 6

stock_price.insert(5, 280)   # arr.insert(index,data)
#  print(stock_price)


'''
order of complexity of insert a element  is O(n).
since we need to shift each data after insertion data.

'''
# delete a element

stock_price.remove(280)   # arr.insert(data)
# print(stock_price)


'''
order of complexity of removal of data  is O(n).
'''

# ====================='code basics exercises'=======================================#

'''

Let us say your expense for every month are listed below

1. january 2200
2. february 2350
3. March 2600
4. April 2130
5. May 2190

create a list to store this monthly expense  and using that find out

1. In feb,how many dollars you spend extra compare to january?
2. Find out your total expense in first quarter of the year(3 months)?
3. find out if you spent exactly 2000 dollars in any month?
4. June month just finished and your expense is 1980 dollars.
Add this item to your monthly expense list?
5. You returned an item that you bought in a month of april
and got a refund of 200$. Make a correction to your monthly expense list? 
'''

expense_list=[2200,2350,2600,2130,2190]

# index_order=[jan,feb,Mar,apr,may]
# 1.

ans=expense_list[1]-expense_list[0]
print(ans)

# 2.

ans=sum(expense_list[0:3])
print(ans)

# 3.

if 2000 in expense_list:
    print("found 2000")
else:
    print("not found")

# 4.
expense_list.append(1980)
print(expense_list)

# 5.

expense_list[3]=expense_list[3]+200
print(expense_list)


'''

You have a list of your favourite marvel super heroes.

hero =['spider man', 'thor', 'hulk', 'iron man', 'captain america']

using this find out

1. length of the list
2. Add 'black panther' at the end of this list
3. You realize you have to add 'black panther' after 'hulk'.
so remove it from the list first and then add it after hulk
4. Now you don't like thor and hulk because they get angry easily.
so you want to remove 'thor' and 'hulk'  from list and replace
them with 'doctor strange'.Do that in one line of code
5. sort the heroes list in alphabetical order(use dir() function to list all available functions)
'''

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1.

length = len(heros)

# 2.
heros.append('black panther')
print(heros)

# 3.
heros.pop()

heros.insert(3,"black panther")
print(heros)

# 4.
heros[1:3]=['doctor strange']
print(heros)

# 5.
heros.sort()
print(heros)

'''

Create a list of all odd numbers between 1 and max numbers .Max number is something you
need to take from user using input() function.

'''

max_value = input(" I can print  even no until a max no.please enter the max value: ")

odd_list = []
for i in range(int(max_value)):
    if (i % 2) != 0:
        odd_list.append(i)
print(odd_list)

# or use list comprehension

odd_list = [i for i in range(int(max_value)) if (i % 2) != 0]
print(odd_list)


