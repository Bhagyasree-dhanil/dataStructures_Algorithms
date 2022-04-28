"""
SETS

represented in curly bracket = {}

unordered, unindexed, Duplicates not allowed.

we can remove and add items in sets.

"""

set_data = {'apple', 'banana', 3, 2, 2, 2}
# print(set_data)

# length of sets
len_set = len(set_data)
# print(len_set)

# Accessing items
for i in set_data:
    print(i)

# check a value is present or not
print("apple" in set_data)

# add items
set_data.add("kiwi")

# add any other iterable objects into sets
set_data.update(["grapes", "orange"])

# remove item
set_data.remove("orange")
set_data.discard("orange")  # same as remove, but discard didn't raise any error while the data is not available.
set_data.pop() # since unordered we didn't get as last item , so not used along with sets

# to empty the sets
set_data.clear()

# delete the sets
del set_data

# join sets by removing duplicates

set1 = {"a", "b", "c"}
set2 = {"1", "2", "3", "c"}

set3 = set1.union(set2)
set4 = set1.update(set2)

# intersection
set5 = set1.intersection_update(set2)
print("intersection_update",set5)