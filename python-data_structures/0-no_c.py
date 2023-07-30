def no_c(my_string):
    space = ""
    for i in range(len(my_string)):
      if(my_string[i] != 'c' and my_string[i] != 'C'):
        space += my_string[i]     
    return space
