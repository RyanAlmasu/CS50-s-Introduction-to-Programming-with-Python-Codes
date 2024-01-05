import sys
import csv
import tabulate

if len(sys.argv) == 2:
    if sys.argv[1][-3:] == 'csv':
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("Not a csv file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")