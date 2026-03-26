#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for i in set_1:
        if i in set_2:
            continue
        else:
            new_list.append(i)
    for i in set_2:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list
