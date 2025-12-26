def first_non_repeating_char(string):
    char_count ={}
    for char in string:
        char_count[char] = char_count.get(char, 0)+1
    non_repeat = []
    for char, count in char_count.items():
        if count == 1:
            non_repeat.append(char)
    if non_repeat:
        return non_repeat[0]
    else:
        return None
    
print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""