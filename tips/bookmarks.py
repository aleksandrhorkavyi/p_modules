# 240

# Notes
# list    [1,2,3]
# set     {1,2,3}
# dict    {"a": 1}
# tuple   (1,2,3)

# vars() - переменные окружения

# процедура - именованная последовательность вычислительных шагов

# функции высших порядков - функции, которые могут принимать
# в качестве агрументов и возвращать другие функции

# мемоизация - сохранение результатов выполнения функции для
# предотвращения повторных вычислений


# 1.4
from pprint import pprint

print('------------ 1.4 ------------')
# Поиск макс и мин элементов
import heapq
"""
если N невелико относительно общей коллекции heapq - збс
"""
nums_1_4 = [76,4,5,6,7,75,-5,7,4,1]
largest_1_4 = heapq.nlargest(3, nums_1_4)
smallest_1_4 = heapq.nsmallest(2, nums_1_4)
"""
самая важная возможность кучи, heap[0] - всегда наименьший элемент 
"""
heapq.heapify(nums_1_4)
for smallest in range(3):
    print(heapq.heappop(nums_1_4))



# 1.5
print('------------ 1.5 ------------')
# Простая очередь с приоритетом

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


queue_1_5 = PriorityQueue()
queue_1_5.push('F', 5)
queue_1_5.push('C', 3)
queue_1_5.push('W', 28)

item_1_5 = queue_1_5.pop()
item2_1_5 = queue_1_5.pop()


# 1.7
print('------------ 1.7 ------------')
# Порядок в словарях чтобы контролировать порядок элементов при итерации
# или сериализации
from collections import OrderedDict
"""
при итерировании он сохраняет порядок добавления данных
"""
d_1_7 = OrderedDict()
d_1_7['one'] = 1
d_1_7['two'] = 2
d_1_7['three'] = 3

for k in d_1_7:
    print(k)

# 1.16
print('------------ 1.16 ------------')
# Фильтрование элементов последовательности
list_1_16 = [1, 4, -6, 5, -7, 2, 3, 3, 76]
""" используем обычный генератор списка """
less_then_five_standard = [x for x in list_1_16 if x < 5]
""" а тут преобразуем в объект генератора """
less_then_five_gen = (x for x in list_1_16 if x < 5)
""" если нельзя выразить через генератор, юзаем filter """
raw_items_1_16 = ['N/A', 1,3,4,5,'r','-',65,5,-5]

def is_int(val):
    try:
        x = int(val)
        return True
    except:
        return False

only_int_1_16 = list(filter(is_int, raw_items_1_16))

# 3.3
print('------------ 3.3 ------------')
# Форматирование чисел
x_3_3 = 1234.56789
""" до 2 знаков """
a_3_3 = format(x_3_3, '0.2f')
""" выравнивание по правому краю в 10 символов """
b_3_3 = format(x_3_3, '>10.1f')
""" кастомный разделитель разрядов """
f_3_3 = format(x_3_3, '0,.1f')

# 3.4
print('------------ 3.4 ------------')
# Работа с бин шестнадц восьмер целыми числами
x_3_4 = 1234
b_3_4 = bin(x_3_4)
o_3_4 = oct(x_3_4)
h_3_4 = hex(x_3_4)

fb_3_4 = format(x_3_4, 'b')
fo_3_4 = format(x_3_4, 'o')
fh_3_4 = format(x_3_4, 'x')


# 4.13
print('------------ 4.13 ------------')
# Создание каналов для обработки больших данных
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(file_pattern, top):
    """
    Находит все имена файлов в дереве каталогов
    которые совпадают с шаблоном маски оболочки
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, file_pattern):
            print(os.path.join(path, name))
            yield os.path.join(path, name)


def gen_opener(file_names):
    """
    Открываем последовательность имен файлов
    производя соответствующий файловый объект
    """
    for file_name in file_names:
        f = open(file_name, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Объединяет цепочкой последовательность итераторов в одну
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Ищет шаблон регулярного выражения в строках
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# Ищем в логах weightloss упоминания про journey
filepath_4_13 = '/Users/aleksandrhorkavyi/Projects/weightloss/frontend/runtime'

# lognames_4_13 = gen_find('*.log', filepath_4_13)
# files_4_13 = gen_opener(lognames_4_13)
# lines_4_13 = gen_concatenate(files_4_13)
# matches_4_13 = gen_grep('php', lines_4_13)
# for match_line in matches_4_13:
#     print(match_line)

# 5.11
print('------------ 5.11 ------------')
# Манипулирование путями к файлам
import os
filepath_5_11 = '/Users/aleksandrhorkavyi/Projects/weightloss/frontend/runtime'

""" получение последнего компонента пути """
last_5_11 = os.path.basename(filepath_5_11)
""" получение имени каталога """
dirname_5_11 = os.path.dirname(filepath_5_11)
filename_5_11 = os.path.join(filepath_5_11, 'some.log')
""" отделение расширения файла """
ext_5_11 = os.path.splitext(filename_5_11)

# 5.13
print('------------ 5.13 ------------')
# Получение содержимого каталога
filepath_5_13 = '/Users/aleksandrhorkavyi/Projects/weightloss/frontend/runtime'
""" список файлов в каталоге """
file_list_5_13 = os.listdir(filepath_5_13)

# 6.2
print('------------ 6.2 ------------')
import json
""" превращаем в json """
user = {
    'name': 'Tim',
    'gender': 'Male',
    'active': True
}

json_str_6_2 = json.dumps(user)
with open('user.json', 'w') as f:
    f.write(json_str_6_2)
with open('user.json', 'r') as f:
    python_dict_6_2 = json.load(f)


from collections import OrderedDict
s = '{"name": "Jeff", "age": 56, "active": true}'
od = json.loads(s, object_pairs_hook=OrderedDict)
class JsonProfile:
    def __init__(self, dict):
        self.__dict__ = dict

profile = json.loads(s, object_hook=JsonProfile)
name = profile.name


# 7.2
print('------------ 7.2 ------------')
# Определение функции которая принимает только именованные аргументы
""" нужно поместить именованные аргументы после аргумента со звездочкой или звездочки """

def recv(maxsize, *, block):
    pass

""" 
можно использовать для определения именованных аргументов
в функциях, которые принимают различное колличество позиционных аргументов
"""
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

min_7_2 = minimum(1,3,-5,6,10)
min2_7_2 = minimum(1,3,-5,6,10, clip=0)

# 7.8
print('------------ 7.8 ------------')
# Если нужно уменьшить кол-во аргументов ф-ции
""" позволяет присваивать фиксированные значения одному или более аргументам """
""" используем functools.partial() чтобы зафиксировать значения аргументов """

from functools import partial

def foo(a,b,c,d):
    return a,b,c,d

base_7_8 = partial(foo, 'A')
res1_7_8 = base_7_8('b', 'c', 'd')
res2_7_8 = base_7_8('W', 'G', 'Y')

s2 = partial(foo, d=700)
s2(1,2,3)
s2(5,6,7)

s3 = partial(foo, 1,2,d=500)
s3("c")
s3("c2")


# 8.3.
print('------------ 8.3 ------------')
# Объекты с поддержкой менеджера контекста with
# по-сути нужно реализовать __enter__() и __exit__()
from socket import  socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.type = type
        self.address = address
        self.family = family
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


# 8.6
print('------------ 8.6 ------------')
# Создание управляемых атрибутов
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, val):
        if not isinstance(val, str):
            raise TypeError('Not a string')
        self._first_name = val

    @first_name.deleter
    def first_name(self):
        self._first_name = None

class Currency:
    def __init__(self, usd):
        self.usd = usd

    @property
    def uah(self):
        return self.usd * 27.7

    @property
    def rub(self):
        return self.usd * 78.5

c = Currency(100)
uah = c.uah

# 8.8
print('------------ 8.8 ------------')
# Расширение свойства в подклассе
class SubPerson(Person):
    @property
    def first_name(self):
        print('extended first_name getter')
        return super().first_name

    @first_name.setter
    def first_name(self, val):
        print('extended first_name setter')
        super(SubPerson, SubPerson).first_name.__set__(self, val)

    @first_name.deleter
    def first_name(self):
        print('extended first_name del')
        super(SubPerson, SubPerson).first_name.__deleter__(self)

# Если нужно расширить только один из методов
class OneMorePerson(Person):

    @Person.first_name.getter # или @Person.first_name.setter @Person.first_name.deleter
    def first_name(self):
        print('extended OneMorePerson first_name getter')
        return super().first_name

# 8.9
print('------------ 8.9 ------------')
# Создание нового типа атрибута класса или экземпляра
""" Пишем класс-дескриптор """
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Must be integer')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

"""
Чтобы использовать дескриптор его экземпляры 
размещаюются как переменные класса
"""
class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 8.10
print('------------ 8.10 ------------')
# Использование лениво вычисляемых свойств
""" Делаем класс-дескриптор """
class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self

        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val

class Connection:
    def __init__(self, conf):
        self.conf = conf

    @lazyproperty
    def db(self):
        print('connection to DB')
        return 'db.my_database'


conn = Connection({'name': 'db_name', 'port': 3306})
print(conn.db)
print(conn.db)


# 8.11
print('------------ 8.11 ------------')
# Упрощение инициализации структур данных общей ф-цией __init__()
class DTO: # Data Transfer Object
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            TypeError('Expected {} arguments {} given'.format(len(self._fields), len(args)))

        for name, val in zip(self._fields, args):
            setattr(self, name, val)


class Car(DTO):
    _fields = ['model', 'max_speed']

audi_8_11 = Car('Audi', 254)
speed_8_11 = audi_8_11.max_speed

""" с поддержкой именованных аргументов """

class NamedArgsDTO:
    _fields = []
    def __init__(self, *args, **kwargs):
        if (len(args) > len(self._fields)):
            TypeError('Expected {} arguments {} given'.format(len(self._fields), len(args)))

        # установка позиционных аргументов
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # установка оставшихся позиционных элементов
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            TypeError('Invalid {} arguments'.format(','.join(kwargs)))


# 8.13
print('------------ 8.13 ------------')
# Реализации модели данных или системы подтипов

class Descriptor:
    """ дескриптор для установки значения """
    def __init__(self, name = None, **opts):
        self.name = name
        for key, val in opts.items():
            setattr(self, key, val)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    """ дескриптор для принудительного определения типов """
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {} type'.format(str(self.expected_type)))
        super().__set__(instance, value)


class Unsigned(Descriptor): # Mixin
    """ дескриптор для принудительного определения значений """
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value must be grater then 0')
        super().__set__(instance, value)


class MaxSized(Descriptor): # Mixin
     def __init__(self, name=None, **opts):
         if 'size' not in opts:
             raise TypeError('Missing "size"')
         super().__init__(name, **opts)

     def __set__(self, instance, value):
         if len(value) >= self.size:
             raise ValueError('Max size ' + str(self.size))
         super().__set__(instance, value)

# Это базовые строительные блоки из которых создается система типов
# Реализкем другие типы данных


class Int(Typed):
    expected_type = int


class UnsignedInt(Int, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass

# Теперь можно определить такой класс
class Stock:
    name = SizedString('name', size=8)
    shares = UnsignedInt('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

stock_8_13 = Stock('name', 34, 43.4)



# 8.14
print('------------ 8.14 ------------')
# Реализация собственных контейнеров
""" создаем класс с поддержкой итераций """
from collections.abc import MutableSequence


class Workouts(MutableSequence):

    def __init__(self, initial = None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, i: int):
        print('Getting...')
        return self._items[i]

    def __setitem__(self, key, value):
        print('Set value {}'.format(str(value)))
        self._items[key] = value

    def __delitem__(self, key):
        print('delete item {}'.format(str(key)))
        del self._items[key]

    def insert(self, index: int, object) -> None:
        print('Inserting')
        self._items.insert(index, object)

    def __len__(self):
        print('count length')
        return len(self._items)


w = Workouts([1,2,3,76])
w.append(354)
l = len(w)


# 8.15
print('------------ 8.15 ------------')
# Делегирование доступа к атрибуту
# Если нужно делегировать много методов можно использовать
# метод __getattr__()

class A_8_15:
    def spam(self, x): ...

    def foo(self):
        return 'foo'


class B_8_15:
    def __init__(self):
        self._a = A_8_15()

    def bar(self): ...

    def baz(self):
        return 'baz'

    def __getattr__(self, item):
        """
        если аттрибута в классе B_8_15 нет то срабатывает
        метод __getattr__ а тут мы делегируем все на A_8_15
        """
        return getattr(self._a, item)


b_8_15 = B_8_15()
bar_8_15 = b_8_15.bar()
baz_8_15 = b_8_15.baz()
foo_8_15 = b_8_15.foo()

""" Маленький Прокси-класс """
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print('getattr', item)
        return getattr(self._obj, item)

    def __setattr__(self, key: str, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('setattr', value)
            setattr(self._obj, key, value)

    def __delattr__(self, item: str):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('delattr', item)
            delattr(self._obj, item)


proxy_8_15 = Proxy(b_8_15)
pfoo = proxy_8_15.foo()
pbaz = proxy_8_15.baz()


# 8.16
print('------------ 8.16 ------------')
# Определение более одного конструктора в классе
""" для этого нужно испольковать метод класса """
import time

class Date:
    def __init__(self, y, m, d):
        """ основной конструктор """
        self.y = y
        self.m = m
        self.d = d

    @classmethod
    def today(cls):
        loctime = time.localtime()
        return cls(loctime.tm_year, loctime.tm_mon, loctime.tm_mday)

    def __str__(self):
        return '{}/{}/{}'.format(self.y, self.m, self.d)

date_8_16 = Date(2020,12,12)
date_today_8_16 = Date.today()


# 8.17
print('------------ 8.17 ------------')
# Создание екземпляра без вызова __init__()
date_8_17 = Date.__new__(Date)


# 8.18
print('------------ 8.18 ------------')
# Расширение класса с помощью Mixins

"""
У миксин не должно быть собственного метода __init__()
и переменных экземпляра
"""

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


# 8.24
print('------------ 8.24 ------------')
# Классы с поддержкой операции сравнения
from functools import total_ordering

class Room:
    def __init__(self, name: str, length: int, width: int):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = []

    @property
    def living_space(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return 'House {}, rooms: {}'.format(self.name, len(self.rooms))

    def __eq__(self, other: 'House'):
        return self.living_space == other.living_space

    def __lt__(self, other: 'House'):
        return self.living_space < other.living_space

new_house_8_24 = House('New house', 'Split')
new_house_8_24.add_room(Room('Kitchen', 8, 6))
new_house_8_24.add_room(Room('Bedroom', 12, 7))

my_house_8_24 = House('My current house', 'Split')
my_house_8_24.add_room(Room('Bedroom', 10, 9))
my_house_8_24.add_room(Room('Kitchen', 5, 6))

my_8_24 = my_house_8_24.living_space
new_8_24 = new_house_8_24.living_space

is_bigger = new_house_8_24 < my_house_8_24


# 9 Метапрограммирование - создание ф-ций и классов,
# чьей задачей является управление кодом (модификация
# генерация, обертывание существующего кода).

# Возможности: декораторы функций, классов и метаклассы

# 9.1, 9.2
print('------------ 9.1|9.2 ------------')
# Создание обертки для функций

from functools import wraps

# wraps - декоратор для моей обертки, чтобы не терять метаданные
# имя, строка документации, аннотации, сигнатура вызова
# особенность @wraps заключается в том, что он делает обернутую
# ф-ю доступной в аттрибуте __wrapped__

# обращение напрямую к обернутой ф-ции
# do_something.__wrapped__()

def timethis(func):
    """ декоратор выводящий время выполнения """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def do_something():
    val = 1
    for i in range(0, 5000000):
        val += i
    return val

val_9_1 = do_something()


# 9.4
print('------------ 9.4 ------------')
# Определение декоратора принимающего аргументы

import logging

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


def foo():
    pass

# пример отсюда: https://tproger.ru/translations/demystifying-decorators-in-python/

def benchmark(iters):

    def run_benchmark(func):
        import time
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(iters):
                responce = func(*args, **kwargs)
            end = time.time()
            print('Total time: {}'.format(end - start))

        return wrapper
    return run_benchmark

@benchmark(5)
def get_page(url):
    import requests
    return requests.get(url)


resp = get_page('https://google.com')

# 9.6
print('------------ 9.6 ------------')
# Декоратор с параметрами и без
domain = 'hooligan.pp.ua'

def normalize(func=None, *, schema = 'https'):
    if func is None:
        return partial(normalize, schema=schema)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return '{}://{}/{}'.format(schema, domain, func(*args, **kwargs))
    return wrapper


@normalize(schema='http')
def create_url(url):
    return url

url = create_url('path/to/action')


# 9.7
print('------------ 9.7 ------------')
# Принудительная проверка  типов в функции с использованием декоратора
from inspect import signature

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func
        # отображаем имена аргументов на предоставленные типы
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # принудительно проверяем типы аргументов ассертами
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, criteria=str)
def foo_9_7(a,b,criteria):
    return a,b,c

var_foo_9_7 = foo_9_7(1, 'q', 'FF')


# 9.8
print('------------ 9.7 ------------')
# Определение декораторов как части класса

class A_9_8:
    # Декоратор как метод экземпляра
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


a_9_8 = A_9_8()

@a_9_8.decorator1
def spam_9_8():
    pass

@A_9_8.decorator2
def foo_9_8():
    pass


# 9.9
print('------------ 9.9 ------------')
# Определение декораторов как классов

# Чтобы обернуть функциюю декоратором результат которой будет
# вызываемым объектом. Чтобы декоратор работал и внутри и снаружи
# определения класса

# Чтобы определить декоратор как экземпляр, нужно реализовать
# методы __call__() и __get__()

import types

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls +=1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return types.MethodType(self, instance)

# применение
@Profiled
def foo_9_9():
    pass

# или
class spam_9_9:
    @Profiled
    def bar(self, x):
        pass


# 9.10
print('------------ 9.10 ------------')
# Применение декораторов к методам класса и статическим методам

# как обичные декораторы только должен быть ниже чем
# @staticmethod или @abstractmethod


# 9.11
print('------------ 9.11 ------------')
# написание декораторов которые добавляют аргументы обернутым функциям
import inspect

def optional_debug(func):
    sig = inspect.signature(func)
    if 'debug' in sig.parameters.keys():
        raise TypeError('debug argument already defined')
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
            return func(*args, **kwargs)
    params = list(sig.parameters.values())
    params.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=params)
    return wrapper


@optional_debug
def foo(x, y):
    return  x * y

foo(1,2)





print(0)
