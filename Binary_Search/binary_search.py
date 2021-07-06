import random
import time
# Implementation of Binary Search Algorithm
# We'll prove that binary search is faster than naive search

# Naive search: Scan entire list and ask if its equal to the target
# If yes, return index
# If no, return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary search uses divide and conquer
# Keep in mind that our list MUST be sorted if we want to use Binary search

def binary_search(l, target, low=None, high=None):
    # Default parameters
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    # Target not found
    if high < low:
        return -1

    # Midpoint of the array (rounded down)
    midpoint = (low + high) // 2

    if l[midpoint] == target: # Target found
        return midpoint
    elif target < l[midpoint]: # Target on low half
        return binary_search(l, target, low, midpoint-1)
    else: # Target on high half
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # Build a sorted list of length 10000
    sorted_list = set() # We use a set in order to avoid having two (or more) equal numbers
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length)) # We add random numbers to the set
    sorted_list = sorted(list(sorted_list)) # Convert the set into a list and sort it

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")