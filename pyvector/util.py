from typing import Any
from types import UnionType


WRONG_TYPE = "{name} should be {suggested_type}, not {given_type}."


def check_type(variable: Any, name: str, suggested_type: type | UnionType | tuple[type | UnionType, ...]):
    assert \
        isinstance(variable, suggested_type), \
        WRONG_TYPE.format(
            name=name,
            suggested_type=suggested_type,
            given_type=type(variable)
        )