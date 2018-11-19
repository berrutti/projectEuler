def isPalindrome(number):
    numberToString = str(number)
    begining = 0
    end = len(numberToString)-1
    while begining < len(numberToString)/2:
        if numberToString[begining] != numberToString[end-begining]:
            return False
        begining += 1
    return True

def findBiggestPalindrome():
    for number in range(999,99,-1):
        for otherNumber in range(999,99,-1):
            result = number * otherNumber
            if isPalindrome(result):
                return result, number, otherNumber

result, firstNum, secondNum = findBiggestPalindrome()

print('The biggest palindrome is:')
print(result)
print('The first number was:')
print(firstNum)
print('The second number was:')
print(secondNum)

