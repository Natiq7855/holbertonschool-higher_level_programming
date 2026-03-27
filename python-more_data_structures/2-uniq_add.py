#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i in new_list:
            continue
        new_list.append(i)
    result = sum(new_list)
    return result
