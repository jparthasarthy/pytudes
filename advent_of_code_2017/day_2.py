input_path = 'day_2_input.txt'

f = open(input_path, 'r')
total = 0
for line in f:

    numbers = list(map(int, line.strip('\n').split('\t')))
    numbers.sort()
    total += numbers[-1] - numbers[0]

print(total)