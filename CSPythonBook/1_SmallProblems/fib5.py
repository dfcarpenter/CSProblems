

def fib5(n: int) -> int:
    if n == 0:
        return n  # special case

    last: int = 0
    next: int = 1

    # last is being set to the previous value of next and next is being set to
    # the previous value of last plus the previous value of next. This avoids the
    # temporary variable to hold the old value of next after last is updated, but
    # before next is updated. Using tuple unpacking in this fashion for some kind of variable
    # swap is common in python
    for _ in range(1, n):
        last, next = next, last + next
    return next


print(fib5(100))