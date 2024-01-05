inputUser = input('Enter the value: ')

print('My Final Value: ', end="")

for i in inputUser:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i , end="")
print()
