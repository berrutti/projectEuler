def isPrime(number, primes):
    for prime in primes:
        if (prime > number/2):
            return True
        if (number % prime == 0):
            return False
    return True

def generatePrimes():
    primes = [2]
    numberToCheck = 3
    while (numberToCheck < 2000000):
        
        if (isPrime(numberToCheck,primes)):
            print('Found a prime:'+str(numberToCheck))
            primes.append(numberToCheck)
        numberToCheck = numberToCheck + 2
    return primes
    
primes = generatePrimes()
print('The primes below two million are: ')
print(primes)
