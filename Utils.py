
def find_key_by_value(d: dict, val, default=None):
    for k, v in d.items():
        if v == val:
            return k
    return default
