
def frequencies(filename):
    total_freq = 0
    f = open(filename, "r")
    for line in f:
        total_freq += int(line)

    return(total_freq)
