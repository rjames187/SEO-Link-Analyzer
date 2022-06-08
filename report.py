def remove_none_values(dic : dict):
    for key, value in list(dic.items()):
        if value == None:
            del dic[key]
    return dic
    
