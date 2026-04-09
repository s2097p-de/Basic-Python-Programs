#Display only those characters which are present at an even index number in given string.
'''
You can solve this using a for loop with a range that steps by 2. Iterate through the characters of the string using a loop and the range() function.
Use start = 0, stop = len(s) - 1, and step = 2. The step is 2 because we want only even index numbers.
Or by using Python’s built-in string slicing syntax [::2].
'''

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size , 2):
    print("index[", i, "]", word[i])