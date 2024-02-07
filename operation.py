class Operation:

    def __init__(self, id, state, date1, operationAmount, description, from1, to):
        self.id = id
        self.state = state
        self.date1 = date1
        self.operationAmount = operationAmount
        self.description = description
        self.from1 = from1
        self.to = to

    def date_conversion(self):
        date_slice = self.date1[:10]
        date_list = date_slice.split('-')
        date_list.reverse()
        date_conversion = '.'.join(date_list)
        return date_conversion

    def from_conversion(self):
        elements = []
        list_from = self.from1.split(' ')
        for element in list_from:
            if element.isalpha():
                elements.append(element)
            else:
                if len(element) < 18:
                    elem = element[:6] + len(element[6:-4]) * '*' + element[-4:]
                    elements.append(elem)
                else:
                    elemen = '**' + element[-4:]
                    elements.append(elemen)
        return ' '.join(elements)

    def to_conversion(self):
        elements = []
        list_to = self.to.split(' ')
        for element in list_to:
            if element.isdigit():
                element = '**' + element[-4:]
            elements.append(element)
        return ' '.join(elements)
