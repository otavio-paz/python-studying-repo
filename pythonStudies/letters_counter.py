def letters_counter (words_list):
    counter = []
    for x in words_list:
        qt = len(x)
        counter.append(qt)
    return counter

if __name__ == '__main__':
    list = ['dog', 'cat']
    total = letters_counter(list)
    print('Total of letters in each word: {}'.format(total))