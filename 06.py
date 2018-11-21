sum = 0
sumOfSquares = 0
for number in range(1,101):
    sum = sum + number
    sumOfSquares = sumOfSquares + number ** 2

squaredSum = sum ** 2
print('The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is')
print(str(squaredSum - sumOfSquares))