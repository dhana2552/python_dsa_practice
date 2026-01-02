# def find_max_min(nums):
#     return max(nums), min(nums)

def find_max_min(nums):
    maximum = minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return maximum, minimum

print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""