# def x(s):
#     l_point = global_len = 0
#     tracker = list()

#     for r_point in s:
#         while r_point in tracker:
#             tracker.pop(l_point)
#             l_point += 1
#         tracker.append(r_point)
#         global_len =max(len(tracker), global_len)
#     return global_len


# def x(s):
#     l_point = global_len = 0
#     tracker = list()

#     for r_point in range(len(s)):
#         while s[r_point] in tracker:
#             tracker.pop(l_point)
#         tracker.append(s[r_point])
#         global_len = max(len(tracker), global_len)
#     return global_len


# x("pwwkew")


# arr = [2, 5, 7, 8, 13, 17]

# num = 7
# ans = 3


# def lin_search(arr: list, num: int) -> int:
#     for i in range(len(arr)):
#         if arr[i] != num:
#             continue
#         else:
#             return i


# def binary_search(arr: list, num:int) -> int:
#     """
#              a
#     2, 5, 7, 8, 13, 17
#             l/m  r
#     """
#     l, r = 0, len(arr) + 1
#     while l != r:
#         # index of guess
#         mid = (l+r)//2

#         if arr[mid] == num:
#             return mid - 1

#         if arr[mid] < num:
#             l = mid + 1

#         if arr[mid] > num:
#             r = mid

#     return mid - 1


# binary_search(arr, 7)
