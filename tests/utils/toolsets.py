from typing import Any, Tuple


def callable_success(onfig: dict[str, Any]) -> Tuple[bool, str]:
    return True, ""


def callable_failure_with_message(config: dict[str, Any]) -> Tuple[bool, str]:
    return False, "Callable check failed"


def callable_failure_no_message(onfig: dict[str, Any]) -> Tuple[bool, str]:
    return False, ""


def failing_callable_for_test(onfig: dict[str, Any]):
    raise Exception("Failure in callable prerequisite")
