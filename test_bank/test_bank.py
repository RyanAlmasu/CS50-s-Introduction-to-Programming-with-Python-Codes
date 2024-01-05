from bank import value

def main():
    test()

def test():
    assert value('Hello') == 0
    assert value('Hello Ry') == 0
    assert value('Hello ry') == 0
    assert value('h') == 20
    assert value('hey') == 20
    assert value('Whats Up?') == 100
    assert value("Good morning") ==  100




if __name__ == "__main__":
    main()