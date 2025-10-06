def print_wrapper(x: int) -> None:
    print(x)
    print(increment_x(x, 5))

def print_new_wrapper(x: int) -> None:
    print(2*x)

def increment_x(x: int, value: int) -> int:
    return x + value

def increment_x(x: int, value: int) -> int:
    return x + value



print_wrapper(1)
