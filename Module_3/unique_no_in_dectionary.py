L = [{"V":"1"}, {"V": "5"}, {"VI": "1"}, {"VI": "5"}, {"VII":"6"}, {"V":"9"},{"VIII":"7"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)
