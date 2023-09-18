"""
What is anagram?
s = 'abcde'  t = 'baedc'
s and t are formed from same characters exactly
if anagram: true else false
Hashmap
time: O(s+t)
space: O(s+t)
"""
# Hashmap
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
        
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True


s = input('enter s: ')
t = input('enter t: ')
print(isAnagram(s,t))


