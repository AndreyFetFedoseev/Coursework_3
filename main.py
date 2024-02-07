from functions import load_list_operations
from functions import executed_operations
from functions import sort_last_five_operations
from operation import Operation

operat = []

list_oper = load_list_operations('operations.json')
list_operations_executed = executed_operations(list_oper)
list_last_opers = sort_last_five_operations(list_operations_executed)

for dict_oper in list_last_opers:
    oper = (
        Operation(id=dict_oper['id'], state=dict_oper['state'], date1=dict_oper['date'],
                  operationAmount=dict_oper['operationAmount'],
                  description=dict_oper['description'], from1=dict_oper.get('from', 'Неизвестно'), to=dict_oper['to']))
    operat.append(oper)

for operation in operat:
    print(f'{operation.date_conversion()}  {operation.description}\n'
          f'{operation.from_conversion()} -> {operation.to_conversion()}\n'
          f'{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n')
