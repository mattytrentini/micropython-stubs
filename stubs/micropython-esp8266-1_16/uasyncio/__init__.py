"""
Module: 'uasyncio.__init__' on micropython-esp8266-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.16', 'name': 'micropython', 'mpy': 9733, 'version': '1.16', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.4.3
from typing import Any


class CancelledError:
    ''

class Task:
    ''

class TaskQueue:
    ''
    def remove(self, *args) -> Any:
        ...

    def peek(self, *args) -> Any:
        ...

    def pop_head(self, *args) -> Any:
        ...

    def push_head(self, *args) -> Any:
        ...

    def push_sorted(self, *args) -> Any:
        ...

def sleep(*args) -> Any:
    ...

def sleep_ms(*args) -> Any:
    ...

def ticks_add(*args) -> Any:
    ...

def ticks_diff(*args) -> Any:
    ...

wait_for : Any ## <class 'generator'> = <generator>
gather : Any ## <class 'generator'> = <generator>

class Event:
    ''
    def __init__(self, *args) -> None:
        ...

    def clear(self, *args) -> Any:
        ...

    def set(self, *args) -> Any:
        ...

    def is_set(self, *args) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>

class Lock:
    ''
    def __init__(self, *args) -> None:
        ...

    def release(self, *args) -> Any:
        ...

    def locked(self, *args) -> Any:
        ...

    acquire : Any ## <class 'generator'> = <generator>
def ticks(*args) -> Any:
    ...


class TimeoutError:
    ''

class SingletonGenerator:
    ''
    def __init__(self, *args) -> None:
        ...


class IOQueue:
    ''
    def __init__(self, *args) -> None:
        ...

    def remove(self, *args) -> Any:
        ...

    def queue_read(self, *args) -> Any:
        ...

    def queue_write(self, *args) -> Any:
        ...

    def wait_io_event(self, *args) -> Any:
        ...

def create_task(*args) -> Any:
    ...

def run_until_complete(*args) -> Any:
    ...

def run(*args) -> Any:
    ...


class Loop:
    ''
    def close(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def create_task(self, *args) -> Any:
        ...

    def run_until_complete(self, *args) -> Any:
        ...

    def call_exception_handler(self, *args) -> Any:
        ...

    def run_forever(self, *args) -> Any:
        ...

    def set_exception_handler(self, *args) -> Any:
        ...

    def get_exception_handler(self, *args) -> Any:
        ...

    def default_exception_handler(self, *args) -> Any:
        ...

def get_event_loop(*args) -> Any:
    ...

def current_task(*args) -> Any:
    ...

def new_event_loop(*args) -> Any:
    ...


class ThreadSafeFlag:
    ''
    def __init__(self, *args) -> None:
        ...

    def set(self, *args) -> Any:
        ...

    def ioctl(self, *args) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>
def wait_for_ms(*args) -> Any:
    ...


class StreamReader:
    ''
    def __init__(self, *args) -> None:
        ...

    def close(self, *args) -> Any:
        ...

    read : Any ## <class 'generator'> = <generator>
    readinto : Any ## <class 'generator'> = <generator>
    readline : Any ## <class 'generator'> = <generator>
    def write(self, *args) -> Any:
        ...

    wait_closed : Any ## <class 'generator'> = <generator>
    aclose : Any ## <class 'generator'> = <generator>
    awrite : Any ## <class 'generator'> = <generator>
    awritestr : Any ## <class 'generator'> = <generator>
    def get_extra_info(self, *args) -> Any:
        ...

    readexactly : Any ## <class 'generator'> = <generator>
    drain : Any ## <class 'generator'> = <generator>

class StreamWriter:
    ''
    def __init__(self, *args) -> None:
        ...

    def close(self, *args) -> Any:
        ...

    read : Any ## <class 'generator'> = <generator>
    readinto : Any ## <class 'generator'> = <generator>
    readline : Any ## <class 'generator'> = <generator>
    def write(self, *args) -> Any:
        ...

    wait_closed : Any ## <class 'generator'> = <generator>
    aclose : Any ## <class 'generator'> = <generator>
    awrite : Any ## <class 'generator'> = <generator>
    awritestr : Any ## <class 'generator'> = <generator>
    def get_extra_info(self, *args) -> Any:
        ...

    readexactly : Any ## <class 'generator'> = <generator>
    drain : Any ## <class 'generator'> = <generator>
open_connection : Any ## <class 'generator'> = <generator>
start_server : Any ## <class 'generator'> = <generator>