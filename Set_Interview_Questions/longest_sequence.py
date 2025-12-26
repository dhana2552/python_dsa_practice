def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    max_counter = 0
    my_set = sorted(set(nums))
    for num in my_set:
        if num-1 not in my_set:
            counter = 1
            while num+1 in my_set:
                counter += 1
                num += 1
            max_counter = max(max_counter, counter)
    return max_counter


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""