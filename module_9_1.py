def apply_all_func(int_list, *functions):
    dict_func_res ={}
    for func_i in functions:
        result_f = func_i(int_list)
        dict_func_res[func_i.__name__] = result_f
    return dict_func_res

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
