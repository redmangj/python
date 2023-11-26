num = int(input())
l = []
divisor = 2
while num > 1:
    if num % divisor == 0:
        l.append(divisor)
        num = num/divisor
    else:
        divisor += 1
print(l)