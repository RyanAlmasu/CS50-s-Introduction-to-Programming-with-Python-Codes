from plates import is_valid

def main():
    test()


def test():

    assert is_valid('HerEE5') == True
    assert is_valid('666663') == False
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False

if __name__ == "__main__":
    main()