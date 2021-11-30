from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(x):
        log = f'{func.__name__}({x}: {type(x)})'
        return log
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

num_list = [2, 5, 7]
c = ''
for i in num_list:
    if num_list.index(i) + 1 == len(num_list):
        b = str(calc_cube(i))
        c = c + b
    else:
        b = str(calc_cube(i))
        c = c + b + ', '
print(c)