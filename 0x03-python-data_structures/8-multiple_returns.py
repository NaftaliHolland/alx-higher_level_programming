#!/usr/bin/python3
def multiple_returns(sentence):
    new_list = list()
    if len(sentence) == 0:
        new_list.append(0)
    else:
        new_list.append(len(sentence))

    new_list.append(sentence[0])
    return tuple(new_list)
