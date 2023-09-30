"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if (number_of_primes <= 0):
        raise ValueError
    
    list = []

    primeCandidate = 1
    count = 0

    while (count < number_of_primes):
        primeCandidate += 1
        if (isPrime(primeCandidate)):
            list.append(primeCandidate)
            count += 1

    return list


def isPrime(number):
    for i in range(2, number):
        if ((number % i == 0) and i != number):
            return False
    return True
