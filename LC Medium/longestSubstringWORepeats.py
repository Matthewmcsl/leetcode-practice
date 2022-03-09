# ==== leetcode MEDIUM ====
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        | Finds the longest running substring within 's'
        """
        # 1. Use two pointers and a 'window' to keep track
        # 2. If the right pointer is at an element that is already in the existing 'window'
        # 3. We keep removing elements from the front until no more duplicates in the 'window'
        # 4. Once we add the new element into our 'window', we compare the new size VS our old size

        largest_size = left_p = 0
        window = set()

        for right_p in range(len(s)):
            while s[right_p] in window:
                window.remove(s[left_p])
                left_p += 1
            window.add(s[right_p])
            largest_size = max(largest_size, len(window))
        return largest_size

if __name__ == '__main__':
    sol = Solution()
    print(f'Test Case #1: s = abcabcbb, longest substring is: {sol.lengthOfLongestSubstring("abcabcbb")}')
    print(f'Test Case #2: s = bbbbbbbb, longest substring is: {sol.lengthOfLongestSubstring("bbbbbbbb")}')
    print(f'Test Case #3: s = abcdefgh, longest substring is: {sol.lengthOfLongestSubstring("abcdefgh")}')