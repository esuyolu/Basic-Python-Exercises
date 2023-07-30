# Write a function named sort_tuple_list,
# which takes a triple tuple list consisting of a name and two separate numbers as parameters,
# and sorts this list according to the first, second, and third elements of the tuple:
# For example:
# [('Tom', 19, 80), ('Json', 22, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json',21, 85)]
# Result:
# [('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Json', 22, 90), ('Tom', 19, 80)]

def sort_tuple_list(tuple_list):
    return sorted(tuple_list)


l = [('Tom', 19, 80), ('Json', 22, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]
print(sort_tuple_list(l))
