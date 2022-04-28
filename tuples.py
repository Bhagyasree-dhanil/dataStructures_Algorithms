"""
Tuple

ordered
indexed
unchangeable
allow duplicates

"""

tuple_data = ("cat", "dog", "mat")
tuple_data1 = tuple(["cat", "dog", "mat"])

# indexing
data1 = tuple_data[0]
data_last = tuple_data[-1]

# update
# first change to list and then update
list_data = list(tuple_data)
list_data[2] = "rat"
new_tuple = tuple(list_data)
print(new_tuple)

# unpacking tuples - extract values back into variable
(animal1, animal2, animal3) = tuple_data
print(animal1, animal2, animal3)

# using asterisk
# if variable is less than tuple data, add an * to the variable name and balance values in tuple will be added as list.
(ani1, *ani) = tuple_data
print(ani1, ani)

# join tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 2  # append same set at end of current set
print(tuple3, tuple4)

# count no of times
tup = (1, 3, 2, 3, 2, 2)
print(tup.count(2))  # no of repeating time
print(tup.index(3))  # first occurrence of value
