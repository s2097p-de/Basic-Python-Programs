#Write a function to remove characters from a string starting from index 0 up to n and return a new string.

"""
Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.

Given Input:

remove_chars("python", 4)
remove_chars("python", 2)

Expected Output:

tive
native
"""
def remove_chars(word, n):
    print('Original string:', word)
    # Extract string from index n to the end
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("Python", 4))
print(remove_chars("Python", 2))