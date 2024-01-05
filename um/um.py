import re

def main():
    print(count(input("Input text: ")))

def count(s):
    return len(re.findall(r"\b[uU]m", s))
if __name__ == "main":
    main()