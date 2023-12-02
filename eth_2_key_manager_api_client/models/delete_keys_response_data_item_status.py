from enum import Enum


class DeleteKeysResponseDataItemStatus(str, Enum):
    DELETED = "deleted"
    ERROR = "error"
    NOT_ACTIVE = "not_active"
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)
