def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)
    print(n - 1, "ended")


# repeat_hello(5)
# 5 ended


def repeat_hello_iterative(n):
  for _ in range(n):
    print("Hello")


# repeat_hello_iterative(5)

# Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.


# Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)


# print(factorial(0)) # expect 1
# print(factorial(4)) # expect 24
# print(factorial(10)) #2628800


def sum_list(lst):
  if len(lst) == 0:
    return 0
  if len(lst) == 1:
    return lst[0]
  else:
    return lst[0] + sum_list(lst[1:])


# Time Complexity O(n)

# Space Complexity O(n)

# print(sum_list([])) # return 0
# print(sum_list([5])) # return 5
# print(sum_list([1,2,3,4])) # return 10
# size 4
# size 3, size 2, size 1,

# Given an integer n, return True if n is a power of two. Otherwise, return `False``.

# An integer n is a power of two if there exists an integer x such that n == 2ˣ.


def is_power_of_two(n):
  if n == 1:
    return True
  elif n % 2 != 0 or n < 1:
    return False
  else:
    return is_power_of_two(n // 2)


# any pusre power of 2 would yield, 1 if recursivley divided by 2
# 15, 15/2 = 7, 7/2 = 3, 3/2 = 1, 4/2 = 2, 2/2 =1 -> true
# print(is_power_of_two(0)) # invalid input False
# print(is_power_of_two(1)) # expect True
# print(is_power_of_two(4)) # expect True
#
# print(2//2)


def binary_search(lst, target):
  # Initialize a left pointer to the 0th index in the list
  # Initialize a right pointer to the last index in the list
  left = 0
  right = len(lst) - 1

  # While left pointer is less than right pointer:
  while left < right:
    mid = (left + right) // 2
    # Find the middle index of the array
    # If the value at the middle index is the target value:
    if lst[mid] == target:
      return mid
    elif lst[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
  return -1
  # Return the middle index
  # Else if the value at the middle index is less than our target value:
  # Update pointer(s) to only search right half of the list in next loop iteration
  # Else
  # Update pointer(s) to only search left half of the list in next loop iteration

  # If we search whole list and haven't found target value, return -1


# print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 10))
# expect 5


# Example Input: lst = [1, 3, 5, 7, 9, 11, 11, 13, 15], target = 11
# l = 0, r = 8,
#
#
def find_last(lst, target):
  left = 0
  right = len(lst) - 1
  last = -1

  while left < right:
    mid = (left + right) // 2
    if lst[mid] == target:
      last = mid
      left = mid + 1
    elif lst[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
  return last


lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
# print(find_last(lst, target)) # expect 6
#  l = 0, r = 8, m = 4
# l = 5, r= 8, m = 6, last = 6
#


def find_floor(lst, x):
  floor_number = None
  left = 0
  right = len(lst) - 1

  while left <= right:
    mid = (left + right) // 2
    if x == lst[mid] or x <= lst[mid]:
      right = mid - 1
    else:

      floor_number = lst[mid]
      left = mid + 1

  return floor_number


# Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5

# Expected Output: 1

print(find_floor([], 3))  # expect -1
print(find_floor([3, 4, 5, 6], 1))  # expect None
print(find_floor([1, 2, 8, 10, 10, 12, 19], 5))  # expect 2

def find_first(list, target):
  left, right = 0, len(list) -1
  first_index = -1
  while left <= right:
      mid = (left + right) //2
      if list[mid] == target:
        first_index = mid
        right = mid - 1 
      elif list[mid] > target:
        right = mid -1
      else:
        left = mid + 1
  return first_index

def find_last(list, target):
  left, right = 0, len(list) -1
  last_index = -1
  while left <= right:
      mid = (left + right)// 2
      if list[mid] == target:
        last_index = mid
        left = mid + 1
      elif list[mid] > target:
        right = mid -1
      else:
        left = mid + 1
  return last_index

# print(find_first([2,4,10,10,10,12,20], 10)) # expect 2
# print(find_last([2,4,10,10,10,12,20], 10)) # expect 4

def find_frequencies(nums):
  freq_map = {}
  i = 0
  while i < len(nums):
    if nums[i] in freq_map:
      i += 1
      continue
    first = find_first(nums, nums[i])
    last = find_last(nums, nums[i])
    freq_map[nums[i]] = last - first + 1
    i = last+ 1
  return freq_map

print(find_frequencies([1, 2, 2, 3, 3, 3, 4]))

def merge(left_arr, right_arr):
	# Initialize an empty list to store the merged result
  result = []
	# Initialize a pointer to iterate over the left input list
  left = right = 0
  while left < len(left_arr) and right < len(right_arr):
    if left_arr[left] > right_arr[right]:
      result.append(right_arr[right])
      right+= 1
    else:
      result.append(left_arr[left])
      left += 1

  while left < len(left_arr):
    result.append(left_arr[left])
    left += 1
  while right < len(right_arr):
    result.append(right_arr[right])
    right += 1
  return result

def merge_sort(lst):
  left, right = 0, len(lst) -1
  mid = (left + right) // 2 

  if left
  merge_sort(lst[left:mid], lst[mid+1:right])