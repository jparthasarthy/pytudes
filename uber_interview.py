"""
Some random code interview question- why is this even in here?

Input: [1,2,3,4,5]
Output: [120, 60, 40, 30, 24]
"""


def product(iterable):
    i = 1
    for n in iterable:
        i *= n
    return i


def new_array(input):
    new = []
    n = len(input)
    x = product(input)
    for i in range(n):
        new.append(x / input[i])
    return new


if __name__ == "__main__":
    print(new_array([1, 2, 3, 4, 5]))
