from file import read_dataset, write_dataset
from helper import print_commands, print_result, read_values
from manager import create, update, delete
from search import search_record


def main(file_path):
    print_commands()
    dataset = read_dataset(file_path)
    while True:
        command = input('Введіть команду зі списку: ')
        if command == 'new':
            values = read_values()
            dataset = create(dataset, values)
        elif command == 'sf':
            value = input('Введіть ім\'я: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sl':
            value = input('Введіть прізвище: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sfl':
            first_name = input('Введіть ім\'я: ')
            last_name = input('Введіть прізвище: ')
            full_name = f'{first_name} {last_name}'
            result = search_record(dataset, command, full_name)
            print_result(result)
        elif command == 'sp':
            value = input('Введіть номер телефону: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sct':
            value = input('Введіть місто: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sc':
            value = input('Введіть країну: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'up':
            phone = input('Введіть номер телефону для оновлення: ')
            data = read_values()
            dataset = update(dataset, phone, data)
        elif command == 'del':
            phone = input('Введіть номер телефону для видалення: ')
            dataset = delete(dataset, phone)
        elif command == 'help':
            print_commands()
        elif command == 'exit':
            write_dataset(dataset, file_path)
            break
        else:
            print('Дана команда недоступна')


if __name__ == '__main__':
    main('database/database.json')
