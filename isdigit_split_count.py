# string = "1234567"
string = "abcdefg"

def is_contain_numbers_only(string):
    isdigit = string.isdigit()
    return isdigit

is_number = is_contain_numbers_only(string)
print(is_number)

is_number = is_contain_numbers_only("12345")
print(is_number)


sentence = "Ala ma kota"

def number_of_words_in_sentence(string):

    list_of_words = string.split()
    number_of_words = len(list_of_words)

    return number_of_words

print(number_of_words_in_sentence(sentence))


from collections import Counter

def count_each_element_in_string(string):
    number_of_each_element = Counter(sentence)
    return number_of_each_element

print(count_each_element_in_string(sentence))

