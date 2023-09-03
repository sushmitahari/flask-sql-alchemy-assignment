#Sushmita Hari
#I used the website GeeksforGeeks in order to understand how to find the values with the common key. I also used W3Schools and Python Docs to understand the set and keys functions
#https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/
#https://www.w3schools.com/python/python_dictionaries_methods.asp
#https://docs.python.org/3/tutorial/datastructures.html#dictionaries
def get_combined_dict(my_dict_1, my_dict_2):
    dictionary = {}
    dictionaryKeys1 = set(my_dict_1.keys()) 
    dictionaryKeys2 = set(my_dict_2.keys())

    #This helps add the values with the common key
    for i in dictionaryKeys1 & dictionaryKeys2:
        dictionary[i] = my_dict_1[i] + my_dict_2[i]

    return dictionary

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)