t_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
 
print("Original list is : " + str(t_list))
 
res = list(zip(*t_list))
 
print("individual list is : " + str(res))