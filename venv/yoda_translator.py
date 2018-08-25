"""Yoda translator e.g.
"Kill you, he will." -> "He will kill you." 
"A Jedi Master, you are not." -> "You are not a Jedi Master." """

def translate(string):
    words = string.split()
    for i, word in enumerate(words):
        if word.find(',') is not -1:
            pivot = i
    return 
