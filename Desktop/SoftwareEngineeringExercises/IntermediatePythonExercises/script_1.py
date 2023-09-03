def get_unique_list(my_list):
    newList =[]
    for i in range(len(my_list)):
        if my_list.count(i)>=1:
            newList.append(i)
    return newList
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)