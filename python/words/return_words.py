import json
import random

# loads dictionary data
with open('words/dictionary.json', 'r') as file:
    dict_data = json.load(file)

# main random word from dictionary function
def get_random_word(file, required_type):
    words = []
    for word, vars in file.items():
        word_types = vars.get("MEANINGS", [])
        for type in word_types:
            if type[0] == required_type:
                words.append(word)
                break
    return random.choice(words)

def get_rand_noun():
    return get_random_word(dict_data, "Noun")

def get_rand_adjective():
    return get_random_word(dict_data, "Adjective")
