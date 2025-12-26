def has_unique_chars(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0)+ 1
    for count in char_count.values():
        if count > 1:
            return False
    return True


print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""