def rotate(nums, k):
    k = k%len(nums)
    nums[:] = nums[-k:] + nums[:-k] #nums[-k:1] slice gets the last k elements of the list. nums[:-k] slice gets all the elements of the list except for the last k elements.

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""