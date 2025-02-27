"""
Module: 'os' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def remove(*args, **kwargs) -> Any:
    ...


sep = "/"  # type: str


class VfsFat:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def rename(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...


class VfsLfs2:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def rename(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...


def chdir(*args, **kwargs) -> Any:
    ...


def dupterm(*args, **kwargs) -> Any:
    ...


def getcwd(*args, **kwargs) -> Any:
    ...


def ilistdir(*args, **kwargs) -> Any:
    ...


def listdir(*args, **kwargs) -> Any:
    ...


def mkdir(*args, **kwargs) -> Any:
    ...


def mount(*args, **kwargs) -> Any:
    ...


def rename(*args, **kwargs) -> Any:
    ...


def rmdir(*args, **kwargs) -> Any:
    ...


def stat(*args, **kwargs) -> Any:
    ...


def statvfs(*args, **kwargs) -> Any:
    ...


def sync(*args, **kwargs) -> Any:
    ...


def umount(*args, **kwargs) -> Any:
    ...


def uname(*args, **kwargs) -> Any:
    ...


def unlink(*args, **kwargs) -> Any:
    ...


def urandom(*args, **kwargs) -> Any:
    ...
