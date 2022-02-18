# z listy imion wypisz jedynie unikalne imiona
# (lista osób biorących udział w szkoleniach – wybierz wszystkich którzy brali udział chociażby w jednym)

def list_only_unique_names(all_names):
    unique_names = set()
    for names in all_names:
        unique_names.add(names)
    return unique_names


list_of_names = ['Paula', 'Ania', 'Krzysiek', 'Szymon', 'Ania']
print(list_only_unique_names(list_of_names))


# mając dwa słowa sprawdź czy są one annagramami

def if_two_words_are_anagrams(word1, word2):
    char_to_occurence_word1 = {}
    char_to_occurence_word2 = {}
    for ch in word1:
        if ch not in char_to_occurence_word1:
            char_to_occurence_word1[ch] = 1
        else:
            n = char_to_occurence_word1[ch]
            char_to_occurence_word1[ch] = n + 1
    for ch in word2:
        if ch not in char_to_occurence_word2:
            char_to_occurence_word2[ch] = 1
        else:
            n = char_to_occurence_word2[ch]
            char_to_occurence_word2[ch] = n + 1
    if char_to_occurence_word1 == char_to_occurence_word2:
        print("These two words are an anagram")
    else:
        print("these two words are not an anagram")

word1 = "krasa"
word2 = "arska"
if_two_words_are_anagrams(word1, word2)


# policzyć ile głosów zdobył każdy kandytad z wyników głosowania podanych niżej:

def count_votes(list_of_votes):
    results_of_voting = {}
    for e in list_of_votes:
        if e not in results_of_voting:
            results_of_voting[e] = 1
        else:
            n = results_of_voting[e]
            results_of_voting[e] = n + 1
    return results_of_voting

votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
print(count_votes(votes))


# convert list of tuples into dictionary

def convert_list_of_tuples_into_dictionary(list_of_tuples):
    output = dict(list_of_tuples)
    return output


input = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(convert_list_of_tuples_into_dictionary(input))


