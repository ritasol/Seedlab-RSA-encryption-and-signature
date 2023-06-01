import random
from math import gcd
from typing import Tuple

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return (public_key, private_key)

def mod_inverse(a: int, m: int) -> int:
    g, x, y = extended_euclidean_algorithm(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m

def extended_euclidean_algorithm(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return (g, x - (b // a) * y, y)

def encrypt(public_key: Tuple[int, int], message: str) -> int:
    e, n =public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(private_key: Tuple[int, int], cipher: int) -> str:
    d, n = private_key
    message = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(message)
