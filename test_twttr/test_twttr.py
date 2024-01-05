from twttr import shorten

def main():
    test()

def test():
    assert shorten("TWITTER") == 'TWTTR'
    assert shorten('twitter') == 'twttr'
    assert shorten("TwItTeR") == 'TwtTR'
    assert shorten('1234') == '1234'
    assert shorten('!?,.') == '!?,.'



if __name__ == "__main__":
    main()