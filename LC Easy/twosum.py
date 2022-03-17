# ==== leetcode EASY ====
# https://leetcode.com/problems/two-sum/
# 
# Given an array of integers nums and an integer target, return indices of the 
# 
# two numbers such that they add up to target. You may assume that each input would 
# have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        | Returns the index of two elements in the list that adds up to the given target
        """
        seen = {}
        for idx, val in enumerate(nums):
            if (target-val) in seen:
                return [idx, seen[target-val]]
            else:
                seen[val] = idx
        

if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([2, 7, 11, 15], 9)
