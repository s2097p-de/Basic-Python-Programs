## Write a program to find how many times the substring “Emma” appears in a given string.

"""
ext analysis and pattern matching are core pillars of programming. This exercise introduces 
searching for a “needle in a haystack,” a fundamental concept for building search engines or data validation tools.

Given Input:

str_x = "Emma is good developer. Emma is a writer"
Expected Output: Emma appeared 2 times
"""

str_x = "Emma is good developer. Emma is a writer"

count=str_x.count("Emma")
print(f"Emma Appeared {count}times")