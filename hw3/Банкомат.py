print('Банкомат')
notes = [1000, 500, 200, 100, 50]
amount = int(input("Введіть сумму яку ви бажаєте зняти: "))

while amount % 50:
    amount = int(input("Невірна сумма, спробуйте ще раз: "))

for one_note in notes:
    num_of_notes = amount // one_note

    if num_of_notes:
            amount -= num_of_notes * one_note
            print(f"{num_of_notes:2} * {one_note:4}")

    if not amount:
        break