# ==== leetcode EASY ====
# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top. Each time you can 
# either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# -- Bottom-up Dynamic Programming --

class Solution:
    def climbStairs(self, n:int) -> int:
        """
        | Returns the total number of possible 1/2 step combinations to reach the top 
        """
        front, back = 1, 1
        temp = 0

        # 1. Iterate through the entire number of steps
        # 2. Keep track of the latest two combinations required for current step
        # 3. Continue to shift until you reach the last step

        for _ in range(n-1):
            temp = front
            front = front + back
            back = temp
        return front

if __name__ == '__main__':
    sol = Solution()
    sol.climbStairs(3)

