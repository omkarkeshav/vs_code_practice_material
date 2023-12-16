print("Hello World")

from collections import Counter

def count_characters(inpt_string):
    char_count = Counter(inpt_string)

    return char_count

input_string = "Hello World"
result = count_characters(input_string)

for char, count in result.items():
    print(f"Character '{char} occurs {count} times")

'''
def count_characters(input_string):
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char,0) + 1
    
    return char_count

input_string = "you are so intelligent man"

result = count_characters(input_string) 

for char, count in result.items():
    print(f"Character '{char}' occurs {count} times.")

'''