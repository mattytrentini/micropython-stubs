
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class DriveBase:
    def drive() -> None: ...
    def drive_time() -> None: ...
    def stop() -> None: ...
class Stop: ...
def wait() -> None: ...