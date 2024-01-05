def main():
    message =  input("Input: ")
    print(shorten(message))



def shorten(word):
    wrd_without_vowels = ""
    while True:
        for i in word:
            if not i.lower() in ['a' , 'i' , 'u' , 'e', 'o']:
                wrd_without_vowels += i
        return wrd_without_vowels
if __name__ == "__main__":
    main()


