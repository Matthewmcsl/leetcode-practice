class Solution:
    def twoSum_twoPointer(self, numbers: list, target: int) -> list:
        """
        Two pointer solution
        """

        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]

            if s < target:
                left += 1

            if s > target:
                right -= 1

    def twoSum_dictionary(self, numbers: list, target: int) -> list:
        seen = dict()

        for idx, val in enumerate(numbers):
            if target - val in seen:
                return sorted([idx + 1, seen[target - val] + 1])

            seen[val] = idx
