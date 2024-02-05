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
    # list_last_operation = 
    return list_last_opers

# 
# operat = []
# for dict_ in list_last_opers:
#     oper_1 = (
#         Operation(id=dict_['id'], state=dict_['state'], date1=dict_['date'], operationAmount=dict_['operationAmount'],
#                   description=dict_['description'], from1=dict_.get('from', 'Неизвестно'), to=dict_['to']))
#     operat.append(oper_1)
# print(operat)
# for operation in operat:
#     print(f'{operation.date_conversion()}  {operation.description}\n'
#           f'{operation.from_conversion()} -> {operation.to_conversion()}\n'
#           f'{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n')
