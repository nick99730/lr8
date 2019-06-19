def log(f):
    def decorated(*args, **kwargs):
        res = f(*args, **kwargs)
        args_str = ', '.join([str(x) for x in args])
        kwargs_str = ', '.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        print('{}({}{}) = {}'.format(f.__name__, args_str, kwargs_str, res))
        return res
    return decorated


@log
def my_sum(a, b):
    return a + b


@log
def my_mul(a, b):
    return a * b


my_sum(1, 2)
my_mul(3, 4)
