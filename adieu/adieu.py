import inflect
p = inflect.engine()
name_ =  []
while True:
    try:
        name = input("Name: ")
        name_.append(name)
    except EOFError:
        print()
        break
output = p.join(name_)
print("Adieu, adieu, to " + output)