print("Другий рівень")
# Покупка продуктів дитиною
a = 30 # продукт 1
b = 45 # продукт 2
c = 15 # продукт 3
v = a+b+c # загальні витрати

s = int(input()) # сумма

while (v > s):
    print("Дайте ще грошей")
    s1 = int(input())
    s += s1
if (v < s):
    print("А можна залишити здачу собі?")
change = s-v #  залишок
if change >= 50:
    print("А ти як думаєш;)")
elif (( change > 10) and (change < 50)):
    print("Можна")
else:
    print("Все одно ти на " + str(change) + "грн нічого собі не купиш, віддавай!")
if change >= 500:
    print("Віддавай!")