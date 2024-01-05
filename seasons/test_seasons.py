from seasons import get_date

def main():
    test_format()
def test_format():
    try:
        assert get_date("1999-01-01") == "Twelve million, three hundred thirty-two thousand, one hundred sixty minutes"
    except EOFError:
        break

if __name__ == "__main__":
    main()