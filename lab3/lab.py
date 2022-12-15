def input_words():
    print("1. Words input.")

    
def sort_words(words):
    print("2. Words sort.")


def print_words(words):
    print("3. Words output.")


def main():
    print_words(sort_words(input_words()))


if __name__ == "__main__":
    main()