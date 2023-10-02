from src import utils

# """Загрузка файла Заказчика operations.json """
operations_list = utils.load_operations()

# """Вывод операций, по заданному количеству x=5 + предварительная сортировка по EXECUTED и дате """
list_ex = utils.sorting_executed(operations_list)
list_1 = utils.get_last_date(list_ex)
list_2 = utils.count_last_operations(list_1, 5)

# """Преобразование к нужному виду Заказчика"""
    #     """# Пример вывода для одной операции:
    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79** **** 6361 -> Счет **9638
    # 82771.72 руб."""

    # - `id` — id транзакциии
    # - `date` — информация о дате совершения операции
    # - `state` — статус перевода:
    #     - `EXECUTED`  — выполнена,
    #     - `CANCELED`  — отменена.
    # - `operationAmount` — сумма операции и валюта
    # - `description` — описание типа перевода
    # - `from` — откуда (может отсутстовать)
    # - `to` — куда

f_data = utils.formatted_data(list_2)

# Вывод статистики и решение задачи
for item in f_data:
    print(item + "\n")
