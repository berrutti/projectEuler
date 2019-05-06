def markNonPrimes(possiblePrime,total,sieve):
    for i in range(possiblePrime*possiblePrime, total, possiblePrime):
        sieve[i] = False

def sumPrimes(total):
    sum = 0
    sieve = [True] * total
    for possiblePrime in range(2, total):
        if sieve[possiblePrime]:
            sum += possiblePrime
            markNonPrimes(possiblePrime,total,sieve)
    return sum

print(sumPrimes(2000000))