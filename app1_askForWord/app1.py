import json
from difflib import get_close_matches

data = json.load(open("app1_askForWord/data.json"))

def translate(word):
    word = word.lower()
    listOfSimiliarWords = get_close_matches(word, data.keys())
    if len(listOfSimiliarWords) > 0:
        word = listOfSimiliarWords[0]
        print("Did you mean %s" % word)
        if word in data:
            return data[word]
        else:
            return "Word is not in dictionary"
    else:
        return "Word is not in dictionary"
        

word = input("Enter word: ")

output = (translate(word))
if type(output) == list:
    i=0
    for item in output:
        i+=1
        print("%s: %s" % (str(i), item))
else:
    print (output)