from secrets import token_bytes
from typing import Tuple

"""
Encrypt a string using a one-time pad.

from_bytes example
7bytes * 8 bits = 56 bits -> convert to 56 bit integer
"""


def random_key(length: int) -> int:

    # generate length random bytes
    tb: bytes = token_bytes(length)

    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR

    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


### 1.4
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0

    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0

    return pi


print(calculate_pi(10000000))

# 1.5
# Towers of Hanoi



