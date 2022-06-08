def remove_none_values(dic : dict):
    for key, value in list(dic.items()):
        if value == None:
            del dic[key]
    return dic

def sort_pages(dic : dict):
    def ret_val(tup : tuple):
        return tup[1]
    lst = list(dic.items())
    lst.sort(reverse=True, key=ret_val)
    return lst
    
