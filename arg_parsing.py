import argparse

MURZIK = '=^..^=______/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    # Добавление позиционного аргумента для имени.
    parser.add_argument('name', help='Имя')
    # Добавление именованного аргумента для фамилии.
    parser.add_argument('-s', '--surname', help='Фамилия')
    # Новый аргумент.
    parser.add_argument(
        '-c',
        '--city',
        help='Город',
        choices=['Chekhov', 'Dublin', 'Minsk', 'Simbirsk'],
    )
    # Новый аргумент.
    parser.add_argument(
        '-m',
        '--murzik',
        action='store_true',
        help=f'Отправить кота Мурзика {MURZIK}'
    )
    args = parser.parse_args()
    parts = []
    # Добавляем приветствие по имени.
    parts.append(f'Hello, {args.name}')
    # Если указана фамилия, то она тоже добавляется к выводу.
    if args.surname is not None:
        parts.append(args.surname)
    # Новое условие для вывода города.
    if args.city is not None:
        parts.append(f'from {args.city}')
    if args.murzik:
        parts.append(MURZIK)
    # Печатаем через пробел все элементы списка parts.
    print(*parts)
