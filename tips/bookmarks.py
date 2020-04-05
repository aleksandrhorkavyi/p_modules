# 240

# Notes
# list    [1,2,3]
# set     {1,2,3}
# dict    {"a": 1}
# tuple   (1,2,3)

# vars() - переменные окружения

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
    print('sooqa')
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











# 281 308 318
print(0)
