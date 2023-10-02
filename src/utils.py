import json
import datetime
def load_operations():
    """Загрузка файла Заказчика operations.json """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
def sorting_executed(data):
    """Сортировка по state =="EXECUTED" """
    data_executed = []
    for item in data:
        state = item.get("state")
        if state =="EXECUTED":
            data_executed.append(item)
    return data_executed

def get_last_date(data):
    """Сортировка по дате: от новых к старым"""
    data_date = sorted(data, key=lambda x: x["date"], reverse=True)
    return data_date

def count_last_operations(data, x):
    """Вывод операций, по заданному количеству x"""
    data = data[:x]
    return data

def date_transfer(string):
    """Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)."""
    date = datetime.datetime.fromisoformat(string)
    date = date.strftime("%d.%m.%Y")
    return date

def card_transfer(string):
    """Маскировка карты
    Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)."""
    # "Visa Classic 4195191172583802"
    # card_change = string[-16:]
    card_change = string[-len(string):-16]+string[-16:-12]+ " "+ string[-12:-10]+"** **** "+string[-4:]
    return card_change


def bank_account_transfer (string):
    """Маскировка счета
    Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета)."""
    # Счет ** 9638
    # account_change = string[-20:]
    account_change = "Счет **"+string[-4:]
    return account_change

def formatted_data(data):
    """Преобразование к нужному виду Заказчика"""
    #     """# Пример вывода для одной операции:
    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79** **** 6361 -> Счет **9638
    # 82771.72 руб."""
    formatted_data = []
    for item in data:
        date = item.get("date")
        description = item.get("description")
        from_info = item.get("from")
        to_info = item.get("to")
        amount = item["operationAmount"]["amount"]
        name = item["operationAmount"]["currency"]["name"]
        date_change = date_transfer(date)

        if from_info == None:
            from_info_ = ""
        elif from_info != None and "чет" in from_info:
            from_info_ = bank_account_transfer(from_info)
        else:
            from_info_ = card_transfer(from_info)

        if "чет" in to_info:
            to_info_ = bank_account_transfer(to_info)
        else:
            to_info_ = card_transfer(to_info)

        formatted_data.append(f"""{date_change} {description} \n{from_info_} -> {to_info_} \n{amount} {name}""")
    return formatted_data

