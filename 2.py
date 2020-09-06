my_list = [3, 500, 9, 7, 13, 49, 777, 57, 5, 99]
#new_list = []
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(new_list)
