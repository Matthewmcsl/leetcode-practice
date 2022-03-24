# ==== leetcode EASY ====
# https://leetcode.com/problems/sqrtx/

# Sqrt(x)

# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or
# operator, such as pow(x, 0.5) or x ** 0.5.


class Solution:
    def sqrt_linearSearch(self, x: int) -> int:
        """
        | Linear search to solve - O(N) time complexity
        """
        if x <= 1:
            return x

        if x == 2:
            return 1

        for i in range(2, x):
            if i * i > x:
                return i - 1

    def sqrt_binarySearch(self, x: int) -> int:
        """
        | Binary search to solve - O(logn) time complexity
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 -> sqrt(10)
        l              m               r -> 5*5=25, too big! (shift r)
        l     m        r                 -> 2*2=4, too small! (shift l)
                 l  m  r                 -> 4*4=16, too big! (shift r)
                l/m r                    -> 3*3=9, too small! (shift l)
                   l/r                   -> when l = r, exit loop, and return l-1 or r-1
        floor division
        """
        if x <= 1:
            return x

        l_point, r_point = 2, x

        while l_point != r_point:
            mid = (l_point + r_point) // 2

            # if guess is x, return the guess
            if mid * mid == x:
                return mid

            # guess too big, shift right pointer down
            if mid * mid > x:
                r_point = mid

            # guess too small, shift left pointer up
            if mid * mid < x:
                l_point = mid + 1

        # loop exits when left pointer = right pointer
        # return the element before it
        return l_point - 1


if __name__ == "__main__":
    sol = Solution()
    print(f"Linear search: {sol.sqrt_linearSearch(8)}")
    print(f"Binary search: {sol.sqrt_binarySearch(8)}")
