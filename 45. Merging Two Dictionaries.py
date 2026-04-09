"""
Write a program that takes two separate dictionaries and merges them into one single dictionary.

Exercise Purpose: This introduces “Key-Value Consolidation.” Merging dictionaries is a common task when
 combining configuration files or user profiles. It also teaches you about “Key Overwriting”—what happens 
 when both dictionaries share the same key.

Given Input:

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

Expected Output:
{'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}

"""
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
print(f"dictonary :{dict1}&{dict2}")

# combining  both
final_dict = dict1 | dict2
print(f"after combining : {final_dict}")