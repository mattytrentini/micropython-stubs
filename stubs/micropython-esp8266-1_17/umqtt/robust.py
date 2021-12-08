"""
Module: 'umqtt.robust' on micropython-esp8266-1.17
"""
# MCU: {'ver': '1.17', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.17', 'name': 'micropython', 'mpy': 9733, 'version': '1.17', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.4.3
from typing import Any


class MQTTClient:
    ''
    def __init__(self, *args) -> None:
        ...

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def log(self, *args) -> Any:
        ...

    DEBUG = False # type: bool
    def set_callback(self, *args) -> Any:
        ...

    def set_last_will(self, *args) -> Any:
        ...

    def ping(self, *args) -> Any:
        ...

    publish : Any ## <class 'closure'> = <closure>
    def subscribe(self, *args) -> Any:
        ...

    wait_msg : Any ## <class 'closure'> = <closure>
    def check_msg(self, *args) -> Any:
        ...

    DELAY = 2 # type: int
    def delay(self, *args) -> Any:
        ...

    reconnect : Any ## <class 'closure'> = <closure>