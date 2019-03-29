from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):
    """
    A stack for the Towers of Hanoi problem
    Last-In-First-Out ( LIFO )
    Uses a list as a backing store
    """

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs = 3

tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    """
    Moving 1 disc ->  base case
    Moving more than 1 disc -> recursive case
    """



