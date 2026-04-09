#  Display only those characters which are present at an odd index number in given string.

# take user input
word = str(input("Enter the word.. "))
print("Original String:", word)

# Check length of word
size = len(word)

print("Printing only odd index chars")

for i in range (1,size,2):
    print("index[", i, "]", word[i])


