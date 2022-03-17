# ==== leetcode MEDIUM ====
# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

import collections


class Solution:
    def groupAnagrams1(self, strs: list) -> list:
        """
        | Takes in a list of strings, and outputs a nested list of grouped anagrams.
        | solution 1 uses a count array with *space complexity* of O(N) - count array not part of space complexity
        | because it does not scale as the input size becomes asymptotically large,
        """
        track = collections.defaultdict(list)
        for ele in strs:
            count_array = [0] * 26
            for letter in ele:
                count_array[ord(letter) - ord("a")] += 1
            track[tuple(count_array)].append(ele)
        return track.values()

    def groupAnagrams2(self, strs: list) -> list:
        """
        | Solving using sorted function and dictionary
        | Time complexity: O(m*nlogn) - due to sorted and for-loop
        """
        track = dict()
        for ele in strs:
            if tuple(sorted(ele)) not in track:
                track[tuple(sorted(ele))] = [ele]
            else:
                track[tuple(sorted(ele))].append(ele)
        return track.values()


if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Algorithm 1: {sol.groupAnagrams1(strs)}")
    print(f"Algorithm 2: {sol.groupAnagrams2(strs)}")
