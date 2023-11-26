# кур'єр
ap = int(input("Номер квартири? "))
n_a = 108 # кількість квартир
n_f = 9 # кількість поверхів
n_a_f = 4 # кількість квартир на поверсі

while ap > n_a:
    ap = int(input("Спробуй ще раз "))

import math
foyer = math.ceil(ap / (n_f * n_a_f))
if foyer > 1:
    floor = math.ceil((ap - n_f * n_a_f * (foyer - 1))/n_a_f)
else:
    floor = math.ceil(ap/n_a_f)

print('Парадне № ' + str(foyer) + ' поверх ' +str(floor))