class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # if the needle is empty, return 0
        	return 0
		# 0, 1, 2, 3, 4
        for i in range(len(haystack) - len(needle) + 1):
          	# 0, 1
            for j in range(len(needle)):
              	# mismatch
              	if haystack[i+j] != needle[j]:
              		break
                # match
                if j == len(needle) - 1:
                  	return i
        return -1