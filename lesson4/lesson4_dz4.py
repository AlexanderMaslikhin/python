
source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
target_list = [elem for elem in source_list if source_list.count(elem) == 1]
print(target_list)
