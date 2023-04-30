guess_word = ['привет', 'пока']
test_list = ['привет', 'пока', 'pker']


x = set(test_list).intersection(set(guess_word))
print(*x)

if any([x for x in guess_word]):
    print('True')
else:
    print('False')
