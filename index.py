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


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


asan = Student('asan', 59)

print(asan.name)


class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print("Dog is running")


dog = Dog()
dog.run()
print(isinstance(dog, Animal))


def run_twice(a):
    a.run()
    a.run()


run_twice(Dog())

print(type(123))
print(type(dog))
print(isinstance(123, (str, int)))
print(dir(dog))


class Boy(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Boy()
s.score = 80  # OK，实际转化为s.set_score(60)
print(s.score)


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return 10


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
