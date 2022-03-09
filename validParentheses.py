# ==== leetcode EASY ====
# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid. An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

class Solution:
    def validParentheses(self, s:str) -> bool:
        """
        
        """
        stack = []
        match = {'(': ')', '[': ']', '{': "}"}
        index = 0
        
        # if first parentheses is a close, automatically fail
        # if length of the string is odd, return false 
        while index != len(s):
            # check if stack is not empty 
            if len(stack) and s[index] == match.get(stack[-1]): # returns None if no k:v match
                stack.pop(-1)
            else:
                stack.append(s[index])
            index += 1
            
        if not stack and index == len(s):
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print('Test Case #1: {}'.format(sol.validParentheses('{([]]]')))
    print('Test Case #2: {}'.format(sol.validParentheses('{')))
    print('Test Case #1: {}'.format(sol.validParentheses('()[{}]')))




