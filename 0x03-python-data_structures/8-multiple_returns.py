#!/usr/bin/python3

def multiple_returns(sentence):
    "Returns a tuple with the length"
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
