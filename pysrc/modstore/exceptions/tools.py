
from typing import Optional

class MethodOverrideError(Exception):
    def __init__(self, message: str, method_name: str, class_name: str, base_class_name: Optional[str]):
        if base_class_name:
            super().__init__(message.format(method_name, class_name, base_class_name))
        else:
            super().__init__(message.format(method_name, class_name))