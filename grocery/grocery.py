dict = {}


while True:
    try:
        my_food = input().upper()
        if my_food not in dict:
            dict[my_food] = 1
        else:
            dict[my_food] += 1
    except EOFError:
        break
lst = sorted(dict.items())
for a, b in lst:
    print(b,a)

