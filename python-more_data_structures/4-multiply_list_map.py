def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda my_list: my_list * number, my_list))
    return new_list
