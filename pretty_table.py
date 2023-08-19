from prettytable import PrettyTable

if __name__ == '__main__':
    # Инициализируем таблицу.
    yp_table = PrettyTable()
    yp_table.field_names = (
        '№ когорты',
        'Кол-во студентов',
        'Средний балл',
    )
    # Добавляем одну строку списком.
    yp_table.add_row([16, 200, 4.5])
    # Добавляем одну строку кортежем.
    # Можно использовать любой итерируемый объект.
    yp_table.add_row((17, 155, 4.7))

    # Добавляем сразу две строки.
    yp_table.add_rows(
        (
            (18, 211, 4.3),
            (19, 300, 5),
        )
    )
    print(yp_table)
