import class_words
import save_files
import random


words_dict = 'words1.json'
user_scores = 'user_scorers.json'


def main():
    my_words_dict = save_files.load_dict(words_dict)
    my_user_scores = save_files.load_dict(user_scores)

    choose_main_menu = 0

    while choose_main_menu != 5:
        choose_main_menu = show_menu()

        if choose_main_menu == 1:
            add_new_word(my_words_dict)
        elif choose_main_menu == 2:
            edit_word(my_words_dict)
        elif choose_main_menu == 3:
            run_quiz(my_words_dict, my_user_scores)
        elif choose_main_menu == 4:
            call_dict(my_words_dict)

    save_files.save_file(words_dict, my_words_dict)


def show_menu():
    print('''
    1. Add new word
    2. Edit word
    3. Word quiz
    4. How much words in dictynory
    5. Exit \n''')

    try:
        user_choose = int(input('Choose one of the items: '))

        while user_choose < 1 or user_choose > 5:
            user_choose = int(input('Choose one of the items: '))

        return user_choose
    except ValueError:
        print('Please enter a valid number between 1 and 5')


def add_new_word(my_dict):
    eng_word = input('Write english word: ').upper()
    rus_word = input('Write russian word: ')

    entry = class_words.Words(eng_word, rus_word)

    if eng_word not in my_dict:
        my_dict[eng_word] = [w.strip() for w in entry.get_rus_word(rus_word).split(',')]
        print(f'Word added - {entry}')
    else:
        print('This word is excist')


def edit_word(my_dict):
    change_word = input('Which word you want change? ')

    if change_word in my_dict:
        my_dict[change_word] = [w.strip() for w in input('Write words ').split(',')]
        print('Word change')
    else:
        print('Word not exist')


def run_quiz(my_dict, my_user_scores):
    score = 0
    user_name = input('What is your name? ')
    words_count = int(input('How much words you want guess '))

    # Получаем список ключей из файла json
    list_my_dict = list(my_dict.keys())

    # Получаем k рандомных слов (ключей) из файла
    random_count_words = random.sample(list_my_dict, k=words_count)

    # Проходимся циклом беря по одному рандомну слову и выводим на консоль слово для перевода
    for k, word in enumerate(random_count_words, 1):
        print(f'{k}: {word}')
        guess_word = [v.strip() for v in input(f'{k}: Write word: ').split(',')]
        value_words = my_dict.get(word)
        result = count_score(value_words, guess_word, score)

        if set(value_words).issubset(set(guess_word)):  # проверка входит ли множество (set) нужный слов во множество (set) введенное от пользователя
            print('''================ \nALL CORRECT''')
            print(f'Your score: {result}')
            print('========================== \n')

        elif any([list_word in guess_word for list_word in value_words]):  # проверка, входит ли хотя бы одно слово введенное пользователем в список
            copy_list = value_words.copy()

            for value in guess_word:
                if value in my_dict.get(word):
                    copy_list.remove(value)
                else:
                    continue
            print('\n==========================')
            print(f'Your score: {result}')
            print('You forget this words:')
            print(*copy_list)
            print('========================== \n')

        else:
            print('\n==========================')
            print('No, you dont guesed no one words:')
            print(*my_dict.get(word), end='\n')
            print(f'Your score: {result}')
            print('========================== \n')

        save_score(user_name, result, my_user_scores)

    save_files.save_file(user_scores, my_user_scores)


def call_dict(my_dict):
    call = my_dict
    print(f'In dictinory have {len(call)} words')


def count_score(get_word, guess_word, current_score):
    for user_word in guess_word:
        if user_word in get_word:
            current_score += 1
    return current_score


def save_score(name, score, my_user_scores):
    if name not in my_user_scores:
        my_user_scores[name] = score
    else:
        if score > my_user_scores.get(name):
            my_user_scores[name] = score
            print(f'Ваш новый рекодр {score}')
        else:
            print(f'Ваш прошедший рекодр = {my_user_scores.get(name)}')


if __name__ == '__main__':
    main()
