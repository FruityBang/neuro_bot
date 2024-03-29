first_tuple = (1, 2, 3, 4, 5)
second_tuple = (2, 4, 5)

#contains_all = all(elem in first_tuple for elem in second_tuple)
#print(contains_all)
for elem in second_tuple:
    print(elem)
    elem in first_tuple