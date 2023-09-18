"""
brute force: time:O(n^2), space: O(1)
Hashmap: time: O(n), space: O(n)
"""

def twoSum(list, target):
    hashmap = {}  # val : index
    for i, n in enumerate(list):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i
        
list = [1,2,3,4,5]
target = 5
print(twoSum(list, target))

    