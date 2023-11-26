size = {'XXS': 8, 'XS': 10, 'S': 12, 'M': 14, 'L': 16, 'XL': 18, 'XXL': 20, 'XXXL': 22}
country = input('Введіть назву країни ')
i_s = input('Введіть міжнародний розмір ')
if country == 'GER':
    country = 28
if country == 'USA':
    country = 0
if country == 'FR':
    country = 30
if country == 'GB':
    country = 16
c_s = size.get(i_s) + country
print(c_s)

