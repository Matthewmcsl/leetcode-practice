# ==== leetcode EASY ====
# https://leetcode.com/problems/maximum-subarray/
#
# Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

from math import inf


class Solution:
    def maxSubArray(nums: list) -> int:
        """
        | Brute force solution, o(n**2) time complexity, exceeds run time limit in Leetcode
        """
        total = -inf
        for l_point in range(len(nums)):
            running_total = 0
            for r_point in range(l_point, len(nums)):
                running_total += nums[r_point]
                total = max(total, running_total)
        return total


if __name__ == "__main__":
    sol = Solution()
    sol.maxSubArray([5, 4, -1, 7, 8])

"""
To optimize with Kandae's Algorithm (DP)... + divide & conquer
"""
