with open('qwe.txt') as inf:
    for line in inf:
        a = (line.replace(';', ' ')).split()
        line = (list(map(int, a)))
        x = line[-2:]
        a, d = map(int, x)
        x = a + (float(d) / 10)
        del(line[-2:])
        y = (sum(line)) // len(line) + (float((sum(line)) % len(line)) / 10)
        if x == y:
            print("true")
        else:
            print("false")