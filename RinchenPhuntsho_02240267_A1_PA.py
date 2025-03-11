def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    return sum(n for n in range(start, end + 1) if is_prime(n))





    
