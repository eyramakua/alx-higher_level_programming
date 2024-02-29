#!/usr/bin/python3
'''
module to find peak
'''


def find_peak(listint):
    '''Function that returns peak value in a list'''
    if listint:
        n = listint[0]
        for j in listint:
            if j > n:
                n = j
        return n
    else:
        return None
