# def count():
#     fs = []
#     for i in range(1, 4):
#         def g(j):
#             def a():
#                 return j * j
#
#             return a
#
#         r = g(i)
#         fs.append(r)
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3())

__author__ = 'chenyi'
# def is_not_empty(s):
#     return s and len(s.strip()) > 0
#
#
# print(list(filter(lambda s:s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])))
import functools

import sys


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()

# init2 = functools.partial(int, 2)
init2 = functools.partial(int, base=10)
args = sys.argv
print(args)
print(init2("100"))
print(int("100", 2))
