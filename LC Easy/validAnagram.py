# ==== leetcode EASY ====
# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

class Solution():
    def isAnagram_original(self, s: str, t: str) -> bool:
        """
        | Checks if string 's' is an anagram of string 't'. 
        """
        d1, d2 = dict(), dict()

        # fundamental check: both strings must have same length before anagram can even be considered
        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            if d1.get(s[idx]) is None:
                d1[s[idx]] = 1
            else:
                d1[s[idx]] += 1

            if d2.get(t[idx]) is None:
                d2[t[idx]] = 1
            else:
                d2[t[idx]] += 1
        
        for ele in d1:
            if d1[ele] != d2.get(ele, 0):
                return False
        return True

    def isAnagram_optimized(self, s: str, t: str) -> bool:
        """
        | Using 1 dictionary/hashmap to test for anagram
        """
        # 1. Iterate through first string 's' and +1 to the K:V of each element in the dictionary
        # 2. If no matching key is found, immediately return False; otherwise,
        # 3. Iterate through second string 't' and -1 from the same dict everytime a matching key is found
        tracker = dict()

        if len(s) != len(t):
            return False
        
        for s_ele in s:
            tracker[s_ele] = 1 + tracker.get(s_ele, 0)
        for t_ele in t:
            if tracker.get(t_ele) is None:
                return False
            else:
                tracker[t_ele] -= 1
        for e in tracker:
            if tracker[e] != 0:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    # Anagram cases
    sol.isAnagram_original(s='mate', t='tame')
    sol.isAnagram_optimized(s='mate', t='tame')
    # Non-anagram cases
    sol.isAnagram_original(s='a', t='at')
    sol.isAnagram_original(s='321[', t='351]')