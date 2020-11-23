import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def trans(word):

    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("did you mean %s instead? enter y if yes, or N if no: " %
                   get_close_matches(word, data.keys())[0]).lower()

        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist"
        else:
            return "we didn't understand your entry"

    else:
        return "The word doesn't exist, please check it."


word = input("enter word: ")
#word = input("enter word: ").lower()

output  = trans(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
