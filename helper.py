def to_dict(list_):
    result = [item.obj_to_dict() for item in list_]
    return result

