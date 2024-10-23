import itertools

def unique_permutations(nums):
    return list(set(itertools.permutations(nums)))
nums = [1, 1, 2]
output = unique_permutations(nums)
for perm in output:
    print(perm)
