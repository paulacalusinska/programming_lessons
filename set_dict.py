def count_number_of_unique_character(string):
    unique_chars = set()
    for ch in string:
        unique_chars.add(ch)
    return len(unique_chars)

print(count_number_of_unique_character("aabbcc"))

def count_each_element_in_string(string):
    char_to_occurence = {}
    for ch in string:
        if ch not in char_to_occurence:
            char_to_occurence[ch] = 1
        else:
            n = char_to_occurence[ch]
            char_to_occurence[ch] = n+1
    return char_to_occurence
print(count_each_element_in_string("abbccc"))