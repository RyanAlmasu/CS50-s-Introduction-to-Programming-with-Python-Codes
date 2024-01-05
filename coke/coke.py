
amount = 50

while amount > 0:

    print('Amount due is : ', amount)
    coinUser = int(input('Insert value: '))
    if coinUser in [25, 10, 5]:
        amount -= coinUser

changedown = abs(amount)

print('Change Owned ', changedown)
