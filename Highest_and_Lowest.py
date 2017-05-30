def high_and_low(numbers):
    ints=list(map(int,numbers.split()))
    return"{} {}".format(max(ints),min(ints))
