'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

1. Brute force Approach
    Time complexity - O(n2)
    Space Complexity - O(1)

2. Two-pass Hash table Approach
    Time complexity - O(n)
    Space Complexity - O(n)

2. One-pass Hash table Approach
    Time complexity - O(n)
    Space Complexity - O(n)
'''

class Solution:
    def twosum1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twosum2(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def twosum3(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i



num = [1, 2,4, 5, 7]
tgt = 5

s1 = Solution()
twoindices = s1.twosum3(num, tgt)
print(twoindices)
