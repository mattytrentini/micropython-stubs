"""
Module: 'builtins' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


class ArithmeticError(Exception):
    """"""


class AssertionError(Exception):
    """"""


class AttributeError(Exception):
    """"""


class EOFError(Exception):
    """"""


Ellipsis: Any  ## <class ''> = Ellipsis


class GeneratorExit:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class ImportError(Exception):
    """"""


class IndentationError(Exception):
    """"""


class IndexError(Exception):
    """"""


class KeyError(Exception):
    """"""


class KeyboardInterrupt(Exception):
    """"""


class LookupError(Exception):
    """"""


class MemoryError(Exception):
    """"""


class NameError(Exception):
    """"""


class NotImplementedError(Exception):
    """"""


class OSError(Exception):
    """"""


class OverflowError(Exception):
    """"""


class RuntimeError(Exception):
    """"""


class StopIteration(Exception):
    """"""


class SyntaxError(Exception):
    """"""


class SystemExit(Exception):
    """"""


class TypeError(Exception):
    """"""


class ValueError(Exception):
    """"""


class ZeroDivisionError(Exception):
    """"""


def abs(*args, **kwargs) -> Any:
    ...


def all(*args, **kwargs) -> Any:
    ...


def any(*args, **kwargs) -> Any:
    ...


class bool:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class bytearray:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def append(self, *args, **kwargs) -> Any:
        ...

    def extend(self, *args, **kwargs) -> Any:
        ...

    def decode(self, *args, **kwargs) -> Any:
        ...


class bytes:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def count(self, *args, **kwargs) -> Any:
        ...

    def endswith(self, *args, **kwargs) -> Any:
        ...

    def find(self, *args, **kwargs) -> Any:
        ...

    def format(self, *args, **kwargs) -> Any:
        ...

    def index(self, *args, **kwargs) -> Any:
        ...

    def isalpha(self, *args, **kwargs) -> Any:
        ...

    def isdigit(self, *args, **kwargs) -> Any:
        ...

    def islower(self, *args, **kwargs) -> Any:
        ...

    def isspace(self, *args, **kwargs) -> Any:
        ...

    def isupper(self, *args, **kwargs) -> Any:
        ...

    def join(self, *args, **kwargs) -> Any:
        ...

    def lower(self, *args, **kwargs) -> Any:
        ...

    def lstrip(self, *args, **kwargs) -> Any:
        ...

    def replace(self, *args, **kwargs) -> Any:
        ...

    def rfind(self, *args, **kwargs) -> Any:
        ...

    def rindex(self, *args, **kwargs) -> Any:
        ...

    def rsplit(self, *args, **kwargs) -> Any:
        ...

    def rstrip(self, *args, **kwargs) -> Any:
        ...

    def split(self, *args, **kwargs) -> Any:
        ...

    def startswith(self, *args, **kwargs) -> Any:
        ...

    def strip(self, *args, **kwargs) -> Any:
        ...

    def upper(self, *args, **kwargs) -> Any:
        ...

    def center(self, *args, **kwargs) -> Any:
        ...

    def decode(self, *args, **kwargs) -> Any:
        ...

    def partition(self, *args, **kwargs) -> Any:
        ...

    def rpartition(self, *args, **kwargs) -> Any:
        ...

    def splitlines(self, *args, **kwargs) -> Any:
        ...


def callable(*args, **kwargs) -> Any:
    ...


def chr(*args, **kwargs) -> Any:
    ...


class dict:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def copy(self, *args, **kwargs) -> Any:
        ...

    def get(self, *args, **kwargs) -> Any:
        ...

    def items(self, *args, **kwargs) -> Any:
        ...

    def keys(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def popitem(self, *args, **kwargs) -> Any:
        ...

    def setdefault(self, *args, **kwargs) -> Any:
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def values(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Any:
        ...


def dir(*args, **kwargs) -> Any:
    ...


def divmod(*args, **kwargs) -> Any:
    ...


def eval(*args, **kwargs) -> Any:
    ...


def exec(*args, **kwargs) -> Any:
    ...


def getattr(*args, **kwargs) -> Any:
    ...


def globals(*args, **kwargs) -> Any:
    ...


def hasattr(*args, **kwargs) -> Any:
    ...


def hash(*args, **kwargs) -> Any:
    ...


def id(*args, **kwargs) -> Any:
    ...


class int:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    @classmethod
    def from_bytes(cls, *args, **kwargs) -> Any:
        ...

    def to_bytes(self, *args, **kwargs) -> Any:
        ...


def isinstance(*args, **kwargs) -> Any:
    ...


def issubclass(*args, **kwargs) -> Any:
    ...


def iter(*args, **kwargs) -> Any:
    ...


def len(*args, **kwargs) -> Any:
    ...


class list:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def append(self, *args, **kwargs) -> Any:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def copy(self, *args, **kwargs) -> Any:
        ...

    def count(self, *args, **kwargs) -> Any:
        ...

    def extend(self, *args, **kwargs) -> Any:
        ...

    def index(self, *args, **kwargs) -> Any:
        ...

    def insert(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def reverse(self, *args, **kwargs) -> Any:
        ...

    def sort(self, *args, **kwargs) -> Any:
        ...


def locals(*args, **kwargs) -> Any:
    ...


class map:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def next(*args, **kwargs) -> Any:
    ...


class object:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def open(*args, **kwargs) -> Any:
    ...


def ord(*args, **kwargs) -> Any:
    ...


def pow(*args, **kwargs) -> Any:
    ...


def print(*args, **kwargs) -> Any:
    ...


class range:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def repr(*args, **kwargs) -> Any:
    ...


def round(*args, **kwargs) -> Any:
    ...


class set:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def copy(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def add(self, *args, **kwargs) -> Any:
        ...

    def difference(self, *args, **kwargs) -> Any:
        ...

    def difference_update(self, *args, **kwargs) -> Any:
        ...

    def discard(self, *args, **kwargs) -> Any:
        ...

    def intersection(self, *args, **kwargs) -> Any:
        ...

    def intersection_update(self, *args, **kwargs) -> Any:
        ...

    def isdisjoint(self, *args, **kwargs) -> Any:
        ...

    def issubset(self, *args, **kwargs) -> Any:
        ...

    def issuperset(self, *args, **kwargs) -> Any:
        ...

    def symmetric_difference(self, *args, **kwargs) -> Any:
        ...

    def symmetric_difference_update(self, *args, **kwargs) -> Any:
        ...

    def union(self, *args, **kwargs) -> Any:
        ...


def setattr(*args, **kwargs) -> Any:
    ...


def sorted(*args, **kwargs) -> Any:
    ...


class str:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def count(self, *args, **kwargs) -> Any:
        ...

    def endswith(self, *args, **kwargs) -> Any:
        ...

    def find(self, *args, **kwargs) -> Any:
        ...

    def format(self, *args, **kwargs) -> Any:
        ...

    def index(self, *args, **kwargs) -> Any:
        ...

    def isalpha(self, *args, **kwargs) -> Any:
        ...

    def isdigit(self, *args, **kwargs) -> Any:
        ...

    def islower(self, *args, **kwargs) -> Any:
        ...

    def isspace(self, *args, **kwargs) -> Any:
        ...

    def isupper(self, *args, **kwargs) -> Any:
        ...

    def join(self, *args, **kwargs) -> Any:
        ...

    def lower(self, *args, **kwargs) -> Any:
        ...

    def lstrip(self, *args, **kwargs) -> Any:
        ...

    def replace(self, *args, **kwargs) -> Any:
        ...

    def rfind(self, *args, **kwargs) -> Any:
        ...

    def rindex(self, *args, **kwargs) -> Any:
        ...

    def rsplit(self, *args, **kwargs) -> Any:
        ...

    def rstrip(self, *args, **kwargs) -> Any:
        ...

    def split(self, *args, **kwargs) -> Any:
        ...

    def startswith(self, *args, **kwargs) -> Any:
        ...

    def strip(self, *args, **kwargs) -> Any:
        ...

    def upper(self, *args, **kwargs) -> Any:
        ...

    def center(self, *args, **kwargs) -> Any:
        ...

    def encode(self, *args, **kwargs) -> Any:
        ...

    def partition(self, *args, **kwargs) -> Any:
        ...

    def rpartition(self, *args, **kwargs) -> Any:
        ...

    def splitlines(self, *args, **kwargs) -> Any:
        ...


def sum(*args, **kwargs) -> Any:
    ...


class super:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class tuple:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def count(self, *args, **kwargs) -> Any:
        ...

    def index(self, *args, **kwargs) -> Any:
        ...


class type:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class zip:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


NotImplemented: Any  ## <class ''> = NotImplemented


class StopAsyncIteration:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class UnicodeError(Exception):
    """"""


class ViperTypeError(Exception):
    """"""


def bin(*args, **kwargs) -> Any:
    ...


def compile(*args, **kwargs) -> Any:
    ...


class complex:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def delattr(*args, **kwargs) -> Any:
    ...


class enumerate:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def execfile(*args, **kwargs) -> Any:
    ...


class filter:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class float:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class frozenset:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def copy(self, *args, **kwargs) -> Any:
        ...

    def difference(self, *args, **kwargs) -> Any:
        ...

    def intersection(self, *args, **kwargs) -> Any:
        ...

    def isdisjoint(self, *args, **kwargs) -> Any:
        ...

    def issubset(self, *args, **kwargs) -> Any:
        ...

    def issuperset(self, *args, **kwargs) -> Any:
        ...

    def symmetric_difference(self, *args, **kwargs) -> Any:
        ...

    def union(self, *args, **kwargs) -> Any:
        ...


def help(*args, **kwargs) -> Any:
    ...


def hex(*args, **kwargs) -> Any:
    ...


def input(*args, **kwargs) -> Any:
    ...


def max(*args, **kwargs) -> Any:
    ...


class memoryview:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def min(*args, **kwargs) -> Any:
    ...


def oct(*args, **kwargs) -> Any:
    ...


class property:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deleter(self, *args, **kwargs) -> Any:
        ...

    def getter(self, *args, **kwargs) -> Any:
        ...

    def setter(self, *args, **kwargs) -> Any:
        ...


class reversed:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class slice:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...
