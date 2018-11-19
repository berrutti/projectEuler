numbers = [11,12,13,14,15,16,17,18,19,20]
number = 20
def canDivide(someNumber):
    for otherNumber in numbers:
        if (someNumber % otherNumber != 0):
            return False
    return True

print('Calculating...')
while True:
    if (canDivide(number)):
        print('The number is:')
        print(number)
        break
    number+=20