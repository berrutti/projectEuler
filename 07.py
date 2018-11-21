def isPrime(number, primes):
    for prime in primes:
        if (prime > number/2):
            return True
        if (number % prime == 0):
            return False
    return True

def findNthPrime(number):
    primes = [2]
    counter = 2
    numberToCheck = 3
    while (number >= counter):
        if (isPrime(numberToCheck,primes)):
            primes.append(numberToCheck)
            counter = counter + 1
        numberToCheck = numberToCheck + 2
    return primes[-1]
    

nth = int(input('Enter the nth prime you want to get: '))
prime = findNthPrime(nth)
print('The nth prime is: '+str(prime))
