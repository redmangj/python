print("fizz-buzz")
fizz = int(input("Введіть fizz: "))
buzz = int(input("Введіть buzz: "))
x = int(input("Введіть x: "))
for i in range(1, x+1):
    if i%fizz==0 and i%buzz==0:
        print('FB')
    elif i%fizz==0:
            print('F')
    elif i%buzz==0:
            print('B')
    else:
        print(i)