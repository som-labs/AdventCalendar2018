f = open("input.txt", "r")
total_freq = 0
freqs = {}
freqs[str(0)] = 0

trobat = False
for line in f:
    total_freq += int(line)
    if total_freq in freqs:
        print ("La primera frequencia repetida es:" + str(total_freq) )
    else:
        freqs[total_freq] = total_freq #Per posar quelcom
        print("guardo " + str(total_freq))


