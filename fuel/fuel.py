def main():
    value = get_inp('Pls Input : ')
    if value <= 0.01:
        print('E')
    elif value >= 0.99:
        print('F')
    else:
        print(f'{value:.0%}')

def get_inp(prompt):
    while True:
        try:

            a = input(prompt)
            split_f = a.split('/')
            liist = []

            for num in split_f:
                liist.append(int(num))

            if liist[0] > liist[1]:
                raise ValueError

        except (ValueError, ZeroDivisionError):
            pass

        else:
            y = liist[0] / liist[1]
            return y

if __name__ == '__main__':
    main()