def find_longest_string(list1):
    result_string = ''
    for string in list1:
        if len(string) > len(result_string):
            result_string = string
    return result_string

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""