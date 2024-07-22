# Question 1

def count_substring(s, sub):
  # 1) Base Case: If the main string length is less than the substring length, return 0.
  # 2) Recursive Case:
  #    - Check if the current segment of the main string starting from index 0 equals the substring.
  #    - If it matches, increment the count and move the starting index by the length of the substring.
  #    - If not, only move the starting index by one.
  # 3) Return the count.

  sub_len = len(sub)
  if len(s) < len(sub):
    return 0
  if s[:sub_len] == sub:
    return 1 + count_substring(s[sub_len:], sub)
  else:
    return 0 + count_substring(s[1:], sub)


# print(count_substring("abcdeabcde", "abc")) # returns 2
# print(count_substring("", "abc")) # returns 0
# print(count_substring("fdsf", "asdjkfhaf")) # returns 0


def count_zeroes(lst):
  left, right=0, len(lst)-1
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == 0:
      left = mid +1
    else:
      right = mid-1
  return left

print(count_zeroes([0, 0, 0, 0, 1, 1, 1]))  # Expected output: 4

# Resursive
# def count_zeroes(lst):
#   # base case
#   if len(lst) == 0:
#     return 0
#   elif len(lst) == 1:
#     if lst[0] == 0:
#       return 1
#     else:
#       return 0
#   mid = len(lst) //2
#   return count_zeroes(lst[:mid]) + count_zeroes(lst[mid:])