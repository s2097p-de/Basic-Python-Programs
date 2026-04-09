# Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1)
"""
 This exercise teaches “Dynamic Collection Management.” Lists are rarely static; being able to modify, expand, and prune them 
 is essential for handling data like shopping carts, user lists, or inventory systems.

Given Input: fruits = ["apple", "banana", "cherry", "date", "elderberry"]

Expected Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']
"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Given Input{fruits}")
# Append function
af = fruits.append("fig")
print(f"After append {fruits}")
# remove function
rf = fruits.remove("banana")
print(f"After remove {fruits}")