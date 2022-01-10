from micropython import const as const
from typing import Any

__version__: str

class MPU9250:
    mpu6500: Any
    ak8963: Any
    def __init__(self, i2c, mpu6500: Any | None = ..., ak8963: Any | None = ...) -> None: ...
    @property
    def acceleration(self): ...
    @property
    def gyro(self): ...
    @property
    def magnetic(self): ...
    @property
    def whoami(self): ...
    def __enter__(self): ...
    def __exit__(self, exception_type, exception_value, traceback) -> None: ...