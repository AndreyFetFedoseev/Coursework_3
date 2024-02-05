import json
from operation import Operation

def load_list_operations(file_name):
    """
    Получаем список вопросов из файла.json
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


# def sorted_last_five(list_file):
#     for dict_operation in list_file:
#
#         last_sort_five = sorted(list_file, key=lambda x: x['date'])
#     return last_sort_five
def get_name(dictionary):
    return dictionary['date']


def load_operation(list_dict):
    """Функция для выбора основного слова"""
    operations = []
    for dict_operation in list_dict:
        if dict_operation.get('state') == 'EXECUTED':
            operations.append(dict_operation)
    return operations

list_oper = load_list_operations('operations.json')
# print(list_oper)
list_operations_executed = load_operation(list_oper)
# operations = []
# for dict_ in list_oper:
#     operations.append(Operation(id=dict_['id'], state=dict_['state'], date=dict_['date'], operationAmount=dict_['operationAmount'], description=dict_['description'], from1='none', to=dict_['to']))
# # list_oper.sort(key=get_name)
# sorted(operations, key=lambda x: x[Operation.date])
# print(list_oper[1].get('date'))
sort_list_operations = sorted(list_operations_executed, key=lambda x: x.get("date"))
list_last_opers = sort_list_operations[-5:]
list_last_opers.reverse()
# for operation in list_oper:
#     sorted(list_oper, key=operation.get('date'))
# print(list_oper)
print(list_last_opers)
for dict_ in list_last_opers[:1]:
    oper_1 = (Operation(id=dict_['id'], state=dict_['state'], date1=dict_['date'], operationAmount=dict_['operationAmount'], description=dict_['description'], from1=dict_.get('from', 'Неизвестно'), to=dict_['to']))
    # operat.append(oper_1)
print(oper_1.date_conversion())
print(oper_1.from_conversion())
