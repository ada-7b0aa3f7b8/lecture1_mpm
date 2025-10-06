def print_wrapper(x: int) -> None:
    print(x)
    print(increment_x(x, 5))


def increment_x(x: int, value: int) -> int:
    return x + value


print_wrapper(1)
