def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            numer , denominator = fraction.split("/")
            new_numer = int(numer)
            new_denominator = int(denominator)
            f = new_numer / new_denominator
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + '%'

if __name__ == '__main__':
    main()