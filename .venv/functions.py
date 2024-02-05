import json
from operation import Operation


def load_list_operations(file_name):
    """
    Получаем список операций из файла.json
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def executed_operations(list_dict):
    """
    Функция для создания списка успешных операций
    """
    operations = []
    for dict_operation in list_dict:
        if dict_operation.get('state') == 'EXECUTED':
            operations.append(dict_operation)
    return operations


def sort_last_five_operations(list_dict):
    """
    Функция для выбора операций отсортированных по дате
    """
    sort_list_operations = sorted(list_dict, key=lambda x: x.get("date"))
    list_last_opers = sort_list_operations[-5:]
    list_last_opers.reverse()
    return list_last_opers
