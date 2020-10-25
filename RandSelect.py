# Brian Savage
# CS 160 - Algorithms
# Coding Assignment 1
# Implementation of RandSelect

import random

startingString = "Looking for value with rank %s in the array:\n%s"
leftRecurse = "Selected %s as the pivot; its rank is %s; Thus, we recurse on left."
rightRecurse = "Selected %s as the pivot; its rank is %s; Thus, we recurse on right."
resultString = "We found the element with rank %s in array to be %s"

def randSelect(array, rank):
    print(startingString % (rank, array))
    if len(array) == 1 or min(array) == max(array):
        return array[0]
    elif rank == 0:
        return min(array)
    elif rank == len(array) - 1:
        return max(array) 
    pivot = array[randPivot(array)]                
    larger, smaller = partition(array, pivot)
    if len(smaller) - 1 == rank:
        return pivot
    elif rank < len(smaller) - 1:
        print(leftRecurse % (pivot, len(smaller) - 1))
        return randSelect(smaller, rank)
    print(rightRecurse % (pivot, len(smaller) - 1))
    return randSelect(larger, rank - len(smaller))

def randPivot(array):
    return random.randint(0, len(array) - 1)

def partition(array, pivot):
    return [i for i in array if i > pivot], [i for i in array if i <= pivot]

if __name__ == "__main__":
    import numpy as np
    array = list(np.random.randint(100000, size=10000000))
    rank = 123456
    print(resultString % (rank, randSelect(array, rank)))
