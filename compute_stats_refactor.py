from statistics import harmonic_mean, variance, stdev

file = 'random_nums.txt'


def read_ints():
    data = []

    with open(file, 'r') as f:
        for line in f:
            num = int(line)
            data.append(num)
    return data


def count():
    data = read_ints()
    i = len(data)
    return i


def summation():
    addition = 0
    data = read_ints()
    for i in data:
        addition += i
    return addition


def average():
    return round(summation()/count())


def get_maximum_and_minimum():
    data = read_ints()
    minimum = data[0]
    maximum = data[0]
    for i in data:
        if minimum > i:
            minimum = i
        if maximum < i:
            maximum = i
    return minimum, maximum


def minimum():
    data = read_ints()
    smallest = data[0]
    for i in data:
        if smallest > i:
            smallest = i
    return smallest


def maximum():
    data = read_ints()
    largest = data[0]
    for i in data:
        if largest < i:
            largest = i
    return largest


def get_harmonic_mean():
    data = read_ints()
    return round(harmonic_mean(data))


def get_variance():
    data = read_ints()
    return round(variance(data))


def standard_dev():
    data = read_ints()
    return round(stdev(data))


if __name__ == '__main__':
    print(f"Data: {read_ints()}")
    print(f"Total: {count()}")
    print(f"Summation: {summation()}")
    print(f"Average: {average()}")
    print(f"Minimum: {minimum()}")
    print(f"Maximum: {maximum()}")
    print(f"Harmonic Mean: {get_harmonic_mean()}")
    print(f"Variance: {get_variance()}")
    print(f"Standard Deviation: {standard_dev()}")




