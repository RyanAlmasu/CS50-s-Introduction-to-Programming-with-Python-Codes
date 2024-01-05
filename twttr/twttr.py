userInput = input('Input : ')

print('Output is : ', end="")
for i in userInput:
    if not i.lower() in ['a' , 'i' , 'u' , 'e', 'o']:
        print(i , end="")
print()