multOfThreeAndFive = []
for number in range(0, 1000, 3):
    multOfThreeAndFive.append(number)

for number in range(0, 1000, 5):
    multOfThreeAndFive.append(number)

print('Multiples:')
print(multOfThreeAndFive)
print()
print('Sum:')
print(sum(multOfThreeAndFive))