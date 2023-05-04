import math

def is_prime(n):
    if n < 0:
        raise ValueError("Input must be a positive integer")
    if n <= 1:
        return False
    def is_divisible(i):
        if i > math.sqrt(n):
            return True
        elif n % i == 0:
            return False
        else:
            return is_divisible(i+1)
    return is_divisible(2)
