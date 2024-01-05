my_input = input("Insert number= ")

a , b , c = my_input.split()
float_a =  float(a)
float_c =  float(c)

if b == '+':
    print(float_a + float_c)
elif b == '-':
    print(float_a - float_c)
elif b == '*':
    print(float_a * float_c)
elif b == '/':
    print(float_a / float_c)