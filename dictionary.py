"""
Dictionary

store data values in key:value pairs

"""
student_list = {
    "name": "Bhagya",
    "city": "Thrissur",
    "age": 25
}

# access elements
print(student_list["name"])
print(student_list.get("name"))
print(student_list.keys())  # return keys
print(student_list.values())  # return values
print(student_list.items())  # return keys and values as tuple pair

# change values
student_list["age"] = 26
student_list.update({"age": 26})
print(student_list)

# Removing items
student_list.pop("city")  # pop - remove the item with key
student_list.popitem()  # remove the last inserted item

student_list.clear()  # empty the dict
del student_list  # delete the dict
