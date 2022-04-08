"""

Hash Map

when we have a key value pair- it is more efficient to use hash maps O(1) than arrays 0(N)
Dictionary is an inbuilt datastructure in python implemented  using hash map.

"""
# Dictionary

my_dict = {'march6': 310,
           'march7': 312,
           'march8': 318,
           'march9': 300,
           'march10': 314}


# print(my_dict['march8'])


# implementing hash map
class HashTable:

    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        ascii_sum = 0
        for i in key:
            ascii_sum += ord(i)
        return ascii_sum % 100

    def add(self, key, value):
        get_key = self.get_hash(key)
        self.arr[get_key] = value

    def get(self, key):
        get_key = self.get_hash(key)
        return self.arr[get_key]

    def __setitem__(self, key, value):  # same as add fn, but applying index operators
        get_key = self.get_hash(key)
        self.arr[get_key] = value

    def __getitem__(self, key):  # same as get fn, but applying index operators
        get_key = self.get_hash(key)
        return self.arr[get_key]

    def __delitem__(self, key):  # same as get fn, but applying index operators
        get_key = self.get_hash(key)
        self.arr[get_key] = None


t = HashTable()
t.add('march 6', 300)
# print(t.arr)
# print(t.get('march 6'))

# using index operators

t['march 7'] = 310
t['march 8'] = 319

del t['march 8']
# print(t.arr)
# print(t['march 8'])

"""
collision handling 

when different keys have same index. They will have same memory spaces.it will cause overwriting and will loss the
previous value. Inorder to prevent collisions ,there are two ways,

1. Separate chaining : when collision happens, it will create list of key : value pairs in same memory location.
when we are using bad hash function, chances are there to get  a long list, which will increase complexity

2. Linear probing : when already a value is present in the memory location, then it will search for next available 
empty slot and store the value init.

"""


# implementing chaining in python

class HashMap:

    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        ascii_sum = 0
        for i in key:
            ascii_sum += ord(i)
        return ascii_sum % self.Max

    # model to add list [('key1',value1),('key2',value2)]

    def __setitem__(self, key, value):  # same as add fn, but applying index operators
        k = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[k]):

            if len(element) == 2 and element[0] == key:
                self.arr[k][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[k].append((key, value))

    def __getitem__(self, key):  # same as get fn, but applying index operators
        k = self.get_hash(key)

        for i in self.arr[k]:
            if i[0] == key:
                return i[1]

    def __delitem__(self, key):  # same as get fn, but applying index operators
        k = self.get_hash(key)
        for idx, element in enumerate(self.arr[k]):
            if element[0] == key:
                del self.arr[k][idx]


t = HashMap()
t["march 6"] = 300
t["march 17"] = 350
t["march 16"] = 380

del t["march 17"]
# print("check", t.arr)
# print(t["march 17"])

# ========================================= Exercise -1 ===========================================================#
'''
'weather.csv' contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

here we only need temperature details, so we use list.
'''

with open('weather.csv', 'r') as file:
    temp_list = []
    for i in file:
        val = i.split(",")
        try:
            temp_list.append(int(val[1][:2]))

        except:
            print("invalid temperature")

    # print(temp_list)

# What was the average temperature in first week of Jan

avg_temp = (sum(temp_list[0:7])) / 7
# print(avg_temp)

# What was the maximum temperature in first 10 days of Jan

max_temp = max(temp_list[0:10])
# print(max_temp)

# ======================== Exercise -2 ========================================================== #


"""
weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer 
following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
Figure out data structure that is best for this problem

here we use dict
"""

with open('weather.csv') as file:
    temp_dict = {}
    for i in file:
        val = i.split(",")
        try:
            temp_dict[val[0]] = int(val[1][0:2])
        except:
            print("invalid data")

    # print(temp_dict)

# What was the temperature on Jan 9?
# print(temp_dict['Jan-09'])

# What was the temperature on Jan 4?
# print(temp_dict['Jan-04'])

# ================================== Exercise 3 ======================================================#
"""
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python 
and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure out why you selected
 that specific data structure.
 'diverged': 2,
 'in': 3,
 'I': 8
"""
import re

with open('poem.txt') as text:
    words = {}
    for i in text:
        split_line = re.sub(r"[^\w\s]", '', i.strip())  # i.strip()- used to remove \n
        split_val = split_line.split(" ")
        for x in split_val:
            try:
                if words[x]:
                    val = words[x]
                    words[x] = val + 1
            except:
                words[x] = 1

    # print(words)

"""
Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video 
tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing.
 Keep MAX size of arr in hashtable as 10.
"""


class HashLinear:

    def __init__(self):
        self.Max = 10
        self.arr = [None for j in range(self.Max)]

    def get_hash(self, key):
        ascii_sum = 0
        for i in key:
            ascii_sum += ord(i)
        return ascii_sum % self.Max

    # model to add list [('key1',value1),('key2',value2)]

    def __setitem__(self, key, value):  # same as add fn, but applying index operators
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, value)

    def __getitem__(self, key):  # same as get fn, but applying index operators
        k = self.get_hash(key)
        if self.arr[k] is None:
            return
        index_list = self.get_index_list(k)
        for idx in index_list:
            element = self.arr[idx]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):  # same as get fn, but applying index operators
        k = self.get_hash(key)
        index_list = self.get_index_list(k)
        for idx in index_list:
            if self.arr[idx] is None:
                print("del", self.arr)
                return
            if self.arr[idx][0] == key:
                self.arr[idx] = None
                return

    def get_index_list(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, h):
        index_range = self.get_index_list(h)
        print("in", index_range)
        for index in index_range:
            val1 = self.arr[index]
            if self.arr[index] is None:
                return index
            if self.arr[index] == h:
                return index
        raise Exception("hash memory full")


tl = HashLinear()
tl["march 6"] = 300
tl["march 17"] = 350
tl["march 16"] = 380
print("1", tl.arr)
del tl["march 16"]
print("2", tl.arr)
print(tl["march 16"])
