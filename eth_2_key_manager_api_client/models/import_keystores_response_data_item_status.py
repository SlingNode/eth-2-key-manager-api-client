from enum import Enum


class ImportKeystoresResponseDataItemStatus(str, Enum):
    DUPLICATE = "duplicate"
    ERROR = "error"
    IMPORTED = "imported"

    def __str__(self) -> str:
        return str(self.value)
