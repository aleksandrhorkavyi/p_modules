# 8.13

# [useful] - крутые фичи


# 5.13.

import os
path = '/Users/aleksandrhorkavyi/Projects/yii2-analytics'
list = os.listdir(path)
files = [file for file in list if os.path.isfile(os.path.join(path, file))]

import glob
md = glob.glob('/Users/aleksandrhorkavyi/Projects/yii2-analytics/*.md')
from pprint import pprint
# pprint(list)

# 5.19.
import tempfile


# 5.21. сериализация
import pickle

class Foo:
    def __init__(self, x):
        self.x = x

serialized_foo = pickle.dumps(Foo(45))
# read about pickle.load(), pickle.dump()


# 6.2 JSON [useful]

import json
from collections import OrderedDict
s = '{"name": "Jeff", "age": 56, "active": true}'
od = json.loads(s, object_pairs_hook=OrderedDict)
class JsonProfile:
    def __init__(self, dict):
        self.__dict__ = dict

profile = json.loads(s, object_hook=JsonProfile)
name = profile.name


# 6.10. Base64

import base64

s = b'hello'
a = base64.b64encode(s)

# 7.1. function with kwargs

def make_element(name, value, **kwargs):
    keyvals = [' %s="%s"' % item for item in kwargs.items()]
    attr_str = ''.join(keyvals)
    return '<{name}{attrs}>{value}<{name}>'.format(name=name, attrs=attr_str, value=value)

span = make_element('span', 'text!', id='form-control')


# 7.2. если нужно обязать передавать в ф-ю именованные аргументы [useful]
def baz(value, *, default):
    return True

baz = baz(default=12, value=44)

def init(keys=None):
    return [] if keys is None else keys
    # писать только x is None

# 7.3 нельзя задать мутабельніе типы как дефолтные в сигнатуре
ini = init()


# 7.7. чтобы переменная бралась во время определения
# а не выполнения пишем [useful]
x = 10
a = lambda y, x=x: x + y
x = 12
b = lambda y, x=x: x + y

ass = a(10)
bss = b(10)


# 8.3. Объекты с поддержкой менеджера контекста with
# по-сути нужно реализовать __enter__() и __exit__() [useful]
from socket import  socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

from functools import partial

with LazyConnection(('www.python.org', 80)) as s:
    sdd = s.send(b'GET /index.html')


# 8.6. Создание управляемых атрибутов [useful]
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        print('name.getter')
        return self._name

    @property
    def age(self):
        print('age.getter')
        return self._age

    @name.setter
    def name(self, value: str):
        print('name.setter')
        self._name = value.capitalize()

    @age.setter
    def age(self, value):
        print('age.setter')
        if not isinstance(value, int):
            raise TypeError('Must be integer')
        self._age = value

person = Person('alex', 23)
age = person.age
name2 = person.name

# 8.9 Создание нового типа атрибута [useful]

class Integer: # Дескриптор
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Not int type')

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y



# 8.10 Lazy property [useful]

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('area: ')
        return math.pi * self.radius ** 2


circle = Circle(4)

print(circle.area)
print(circle.area)


# 8.11 Упрощение инициализации структур данных [useful]

class Structure:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

class Man(Structure):
    _fields = ['age', 'name']

man = Man(34, 'Alex')


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid arguments {}'.format(','.join(kwargs)))

class Woman(Structure):
    _fields = ['age', 'name', 'siski']

woman = Woman(23, 'Some Name', siski=3)


# 8.12. Interface and Abstract class [useful]

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data: str):
        pass

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data: str):
        pass

socket = SocketStream()

import io

IStream.register(io.IOBase)

# 8.16

from datetime import time

class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def now(cls):
        tim = time.localtime()


# 8.18 Mixins [useful]

class LoggedMappingMixin:
    # типа чтобы низя было указать свойства
    __slots__ = ()

    def __getitem__(self, item):
        print('get {}'.format(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('set {} = {}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('delete item {}'.format(key))
        return super().__delitem__(key)


class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()

d['x'] = 34
d['y'] = 23
y = d['y']




print(0)










