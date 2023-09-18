"""
Hashmap: time:O(m*n), space:O(m)
"""

def groupAnagrams(strs):
    res = {} # mapping character count to list of anagrams
    for s in strs: 
        count = [0]*26 # a ... z
        for c in s:
            count[ord(c)-ord('a')] += 1 
        count_tuple = tuple(count)
        
        if count_tuple not in res:
            res[count_tuple] = []
            
        res[count_tuple].append(s)
    return res.values()

list = ["abc", "cab", "tan", "nat", "cde"]
print(groupAnagrams(list))