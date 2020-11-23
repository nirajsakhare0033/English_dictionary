from PyDictionary import PyDictionary
dictionary = PyDictionary()

def trans(word):
    word = word.lower()

    if word in dictionary:
        return PyDictionary(word)

    else:
        return "the word doest exist"

word = PyDictionary.meaning(input("enter word: "))

print(word)