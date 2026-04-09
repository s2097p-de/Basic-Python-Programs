# Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

# Take user input
text = str (input("Enter the word "))
print(f"Original word is {text}")

# reverse Word
re_word = text[::-1]
print(f"Reverse of the word is {re_word}")