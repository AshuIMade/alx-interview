#!/usr/bin/python3
"""Method for compute the minimum number
    of operations for task Copy All and Paste"""


def minOperations(n):
    """Fewest number of operations needed
    
    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    num_operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            num_operations += min_operations
            n /= min_operations
        min_operations += 1
    return num_operations