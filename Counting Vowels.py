def count_vowels(input_string):
    vowels = input()
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

string = "john jose"
print(f"Number of vowels in '{string}': {count_vowels(string)}")
