
def frequencies2(filename):
    total_freq = 0
    freqs = set([0])

    trobat = False
    while not trobat:
        f = open(filename, "r")
        for line in f:
            total_freq += int(line)
            trobat = total_freq in freqs
            if trobat:
                return total_freq
                break
            else:
                freqs.add(total_freq)
