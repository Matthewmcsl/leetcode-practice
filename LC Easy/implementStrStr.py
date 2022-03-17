# ==== leetcode EASY ====
# https://leetcode.com/problems/implement-strstr/
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not
# part of haystack. Return 0 if needle is empty.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the first index of a substring that is a subset of the haystack
        """
        # if needle is empty, return 0
        if not needle:
            return 0

        # if length of haystack is < than needle, return -1
        if len(haystack) < len(needle):
            return -1

        # the last index to check should be first index of the needle
        for i in range(len(haystack) - len(needle) + 1):
            # if first ele in needle doesn't match iteration's index, skip and move to next haystack index
            if haystack[i] != needle[0]:
                continue
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(f"hello -> ll, index: {sol.strStr('hello', 'll')}")
    print(f"aaaaa -> bba, index: {sol.strStr('aaaaa', 'bba')}")
