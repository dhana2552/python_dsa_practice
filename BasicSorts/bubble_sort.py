def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1): #(5, 0, -1) i = 5, 4, 3, 2, 1, 0
        for j in range(i): # i= 5 j= 0, 1, 2, 3, 4, 5 | i = 4 j = 0, 1, 2, 3, 4 | i =3 j = 0, 1, 2, 3 | i =2 j = 0, 1, 2 | i= 1 j = 0, 1 | i = 0 j = 0
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


print(bubble_sort([4,2,6,5,1,3]))

 
 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
"""