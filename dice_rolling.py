import random

dices = {
    1: ('┌─────────┐',
        '│         │',
        '│    ●    │',
        '│         │',
        '└─────────┘'),

    2: ('┌─────────┐',
        '│  ●      │',
        '│         │',
        '│      ●  │',
        '└─────────┘'),

    3: ('┌─────────┐',
        '│  ●      │',
        '│    ●    │',
        '│      ●  │',
        '└─────────┘'),

    4: ('┌─────────┐',
        '│  ●   ●  │',
        '│         │',
        '│  ●   ●  │',
        '└─────────┘'),

    5: ('┌─────────┐',
        '│  ●   ●  │',
        '│    ●    │',
        '│  ●   ●  │',
        '└─────────┘'),     

    6: ('┌─────────┐',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '└─────────┘')    
}

dice_list = []
total = 0

while True:
    try:
        dice_num = int(input('Eai :) \nQuantos dados quer jogar?\n'))
    except ValueError:
        print('\n--> Apenas números inteiros. :)\n')
        continue
    break

for dice in range(dice_num):
    dice_list.append(random.randint(1,6))

for line in range(5):
    for dice in dice_list:
        print(dices.get(dice)[line], end ='')
    print()

for dice in dice_list:
    total+= dice

print(f'Total: {total}')
