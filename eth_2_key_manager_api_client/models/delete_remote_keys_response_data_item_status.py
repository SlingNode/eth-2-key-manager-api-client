from enum import Enum


class DeleteRemoteKeysResponseDataItemStatus(str, Enum):
    DELETED = "deleted"
    ERROR = "error"
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)
