input_path = 'day_2_input.txt'

f = open(input_path, 'r')
total = 0
for line in f:

    numbers = list(map(int, line.strip('\n').split('\t')))
    total += max(numbers) - min(numbers)

print(total)