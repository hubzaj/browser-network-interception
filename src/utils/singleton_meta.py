from threading import Lock
from typing import Any


class SingletonMeta(type):
    __instances: dict = {}
    __lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        with cls.__lock:
            if cls not in cls.__instances:
                instance = super().__call__(*args, **kwargs)
                cls.__instances[cls] = instance
            return cls.__instances[cls]
