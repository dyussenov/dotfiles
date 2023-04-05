def foo(a,b):
    return a+b


def foo_dec(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return foo(a,b)
    else:
        return None

