
from typing import Optional

class MethodOverrideError(Exception):
    """`Generic Method Override Error Exception.`"""
    def __init__(
            self,
            message: str,
            method_name: str,
            class_name: str,
            base_class_name: Optional[str],
    ) -> None:
        """raise Method Override Error."""