from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


for i in fib6(20):
    print(i)

