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
  if len(lst) <= 1:
    return lst 
  
  mid = len(lst) //2
  left_half = merge_sort(lst[:mid])
  right_half = merge_sort(lst[mid:])

  return merge(left_half, right_half)

print(merge_sort([4, 1, 5, 2, 6, 3, 7]))