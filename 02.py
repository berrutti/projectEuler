result = 0

firstTerm = 1
secondTerm = 2
nextTerm = 0

print('Terms:')
while (nextTerm<=4000000):
    nextTerm = firstTerm + secondTerm
    firstTerm = secondTerm
    secondTerm = nextTerm
    if (nextTerm%2 == 0):
        print(nextTerm)
        result = result + nextTerm
print()
print('Sum:')
print(result)


