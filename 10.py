class Pair(object):
    def __init__(self, number, boolean):
        self.number = number
        self.isPrime = boolean

def generateArray():
    possiblePrimes = []
    for number in range(2000000):
        possiblePrimes.append(Pair(number,True))
    return possiblePrimes

def markMultiples(index,possiblePrimes):
    jump = index
    while (index < 2000000):
        index = index + jump
        possiblePrimes[index].isPrime = False

sum = 0    
possiblePrimes = generateArray()
possiblePrimes[0].isPrime = False
possiblePrimes[1].isPrime = False

for index in range(2000000):
    if (possiblePrimes[index].isPrime):
        sum = sum + possiblePrimes[index].number
        markMultiples(index,possiblePrimes)

#Remove 0 and 1 which are not primes
possiblePrimes.pop(0)
possiblePrimes.pop(0)


print('The sum of all primes below 2000000 is: ')
print(sum)
    
