class Solution:
    def reverse(self, x: int) -> int:
        """
        turn int into a string

        -123 = flip to positive? -123 + 123 + 123
        """

        if x < 0:
            res = int(str(x)[0] + str(x)[:0:-1])
        else:
            res = int(str(x)[::-1])

        return res if res in range(-(2**31), 2**31) else 0


sol = Solution()
sol.reverse(-153)
