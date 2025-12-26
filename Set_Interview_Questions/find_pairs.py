def find_pairs(arr1, arr2, target):
    output = []
    for i in arr1:
        for j in arr2:
            if i+j == target:
                output.append((i, j))
    return output



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""