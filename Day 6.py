# No specific task
# In place of task, I have written the code to find the number of vowels in a string
# Completed

def vowel_count(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(vowel_count("hello"))