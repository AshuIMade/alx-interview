#!/usr/bin/python3
"""
Function to unock boxes with keys
"""


def canUnlockAll(boxes):
    '''
    N number of locked boxes each box is numbered 
    sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    '''

    list_keys = [0]
    for i in list_keys:
        for j in boxes[i]:  # recorro cada caja y anado las keys
            if j < len(boxes) and j not in list_keys:
                list_keys.append(j)
        if len(list_keys) == len(boxes):
            return True
    return False
