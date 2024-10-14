def is_empty(value):
    if value is False:
        return True
    if value in (0, 0.0, 0j):  # 包含整数、浮点数和复数的零
        return True
    if value == "":
        return True
    if value is None:
        return True
    if isinstance(value, (list, tuple, set)):
        return len(value) == 0
    if isinstance(value, dict):
        return len(value) == 0
    if isinstance(value, float) and (value != value):  # 检查 NaN
        return True
    return False

def is_not_empty(value):
    return not is_empty(value)

def key_exists_in_dict(d, key):
    """ 检查字典中是否存在指定的键 """
    return key in d

def key_value_is_empty(d, key):
    """ 检查字典中指定键的值是否为空 """
    if key_exists_in_dict(d, key):
        return is_empty(d[key])
    return True 