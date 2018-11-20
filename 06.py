primes = [1,2,3]
number = 1
counter = 3
nth = 5

def isPrime(someNumber):
    for prime in primes:
        if (prime > someNumber/2):
            return True
        if (someNumber % prime == 0):
            return False
    return True

print('Calculating...')
while True:
    if (isPrime(number)):
        primes.append(number)
        counter = counter + 1
        print('The number is:')
        print(number)

    if (counter == nth):
        print('The nth prime is: ')
        print(number)
        break
    number+=2

