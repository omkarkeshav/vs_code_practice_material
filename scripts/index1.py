print("Hello World")

from collections import Counter

def count_characters(inpt_string):
    char_count = Counter(inpt_string)

    return char_count

input_string = "Hello World"
result = count_characters(input_string)

for char, count in result.items():
    print(f"Character '{char} occurs {count} times")