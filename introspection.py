def introspection_info(obj):
    info = {
        'type': type(obj),
        'attribytes': [i for i in dir(obj) if not i.startswith('_')],
        'methods': [],
        'module': getattr(obj, '__module__', '__main__'),
    }
    return info


x = 42
result = introspection_info(x)
print(result)
