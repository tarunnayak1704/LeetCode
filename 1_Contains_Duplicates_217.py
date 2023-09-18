"""
Brute force approach: Time: O(n^2), Space: O(1)
2nd approach: Sort first; Time: O(nlogn), Space: O(1)
3rd approach: HashSet; Time: O(n), Space: O(n)
"""
import time

start_t1 = time.time()
# Brute force
def containsDuplicate_1(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False
end_t1 = time.time()

start_t2 = time.time()
# Sorting
def containsDuplicate_2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False
end_t2 = time.time()

start_t3 = time.time()
# Hash set
def containsDuplicate_3(nums):
    hashset = set()  # empty set
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
end_t3 = time.time()

start_t4 = time.time()
# Hash map
def containsDuplicate_4(nums):
    hashmap = {}  #empty dictionary
    for n in nums:
        if n in hashmap:
            return True
        hashmap[n] = 1
    return False
end_t4 = time.time()

#n = int(input("Enter the number of elements: "))
#my_list = [int(input(f"Enter element {i+1} of the list: ")) for i in range(n)]
my_list = list(range(10000))
my_list.append(9999)
#print(my_list)
print(f"Brute force: {containsDuplicate_1(my_list)}; time taken: {(end_t1-start_t1)*1000: .4f}ms")
print(f"Sorting: {containsDuplicate_2(my_list)}; time taken: {(end_t2-start_t2)*1000: .4f}ms")
print(f"Hash set: {containsDuplicate_3(my_list)}; time taken: {(end_t3-start_t3)*1000: .4f}ms")
print(f"Hash map: {containsDuplicate_4(my_list)}; time taken: {(end_t4-start_t4)*1000: .4f}ms")