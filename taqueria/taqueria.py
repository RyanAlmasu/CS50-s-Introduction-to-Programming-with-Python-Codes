def main():
    order = get_order('What would you like to order? ')
    if order != 'control-d' and 4.00 <= order <= 11.00:
        None

def get_order(order):
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    price = 0
    while True:
        try:
            customer_order = input(order).title().strip()

            price += menu[customer_order]

            print('$' + f'{price:.2f}')

        except EOFError:
            return price
        except KeyError:
            pass




main()