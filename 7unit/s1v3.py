# UNIT 7 Version 3

def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + '*' + insert_stars(s[1:])

# print(insert_stars('abc'))

def insert_stars_iterative(s):
    result_arr = []
    for i in range(len(s)):
        if i == len(s) - 1:
            result_arr.append(s[i])
        else:
            result_arr.append(s[i])
            result_arr.append("*")

    return ''.join(result_arr)

# s = "asdf"
# print(insert_stars_iterative(s))

def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])

# print(string_length(""))

def sum_digits(n):
    if n >= 0 and n < 10:
        print(n)
        return n
    else:
        print(n)
        return (n % 10) + sum_digits(n // 10)

# print((sum_digits(9876)))

def count_sevens(n):
    if n == 0:
        return 0
    elif (n % 10) == 7:
        return 1 + count_sevens(n // 10)
    else:
        return count_sevens(n // 10)

# print(count_sevens(72117))

# def binary_search(list, target):
#     left = 0
#     right = len(list) -1
#     while left <= right:
#         mid = (left + right) // 2
#         print(list[mid])
#         if list[mid] == target:
#             return True
#         elif target > list[mid]:
#             left = mid - 1
#         else:
#             right = mid + 1
#     return False

# print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 5))

def find_missing(nums):
    left, right = 0 , len(nums)
    while left < right:
        mid = (left + right)//2
        if nums[mid] > mid:
            right = mid
        else:
            left = mid + 1
    return left

# print(find_missing([3,4,5])) # can this be an input??
# print(find_missing([0,1,2,3,4])) # returns 6 which is missing

def sqrt(x):
    pass