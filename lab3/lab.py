def input_words():
    print("\n1. Words input.")
    return input().split()

    
def sort_words(words):
    '''
    Sorts list of words alphabetically
    '''
    print(f"\n2. Words sort.\n{words} -> ", end='')
    
    n = len(words)

    # bubble sort
    for i in range(n):
        for j in range(i + 1, n):
            if words[i] > words[j]:
                word = words[i]
                words[i] = words[j]
                words[j] = word
    print(words)

    return words


def print_words(words):
    print("\n3. Words output.")
    print(*words)


def main():
    print_words(sort_words(input_words()))


if __name__ == "__main__":
    main()