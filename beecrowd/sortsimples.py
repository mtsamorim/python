numbers = [int(x) for x in input().split()]
numbers2 = []

for x in numbers:
    numbers2.append(x)

for x in range(int(len(numbers))-1):
    for i in range(int(len(numbers))-1):
        if numbers[i+1] < numbers[i]:
            aux = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = aux

for x in numbers:
    print(x)

print()

for x in numbers2:
    print(x)