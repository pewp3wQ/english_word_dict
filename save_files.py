import json
import os


def save_file(file_name, data_to_save):
    with open(file_name, 'w', encoding='utf-8') as save:
        json.dump(data_to_save, save, ensure_ascii=False, indent=4)


def load_dict(file_name):
    file = {}

    try:
        # Проверяем, что файл слов существует и не пустой
        if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name, 'r', encoding='utf-8') as f:
                file = json.load(f)
    except FileNotFoundError:
        print('File not found.')
    except json.decoder.JSONDecodeError:
        print('Error loading JSON file.')

    return file
