with open('fb.txt') as a:
    for line in a:
        f, b, x = map(int, line.split())
        result = []
        for i in range(1, x + 1):
            if i % f == 0 and i % b == 0:
                result.append('FB')
            elif i % f == 0:
                result.append('F')
            elif i % b == 0:
                result.append('B')
            else:
                result.append(str(i))
        inf =' '.join(result)
        print(inf)


        with open('fb1.txt', 'a') as c:
            c.write(inf + "\n")