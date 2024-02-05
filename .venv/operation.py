import datetime

class Operation:

    def __init__(self, id='fetid', state='fetstate', date1='fetdate', operationAmount='fetoA', description='fetd', from1='fetfrom', to='fetto'):
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


    def description_conversion(self):
        return self.description


    def from_conversion(self):
        # i = 1
        # elements = []
        # for element in self.from1:
        #     print(element)
        #     if element.isalpha():
        #         continue
        #     elif 0 < element.isdigit() < 18:
        #         if 6 < i < 13:
        #             element = '*'
        #         i += 1
        #     elif element.isdigit() > 18:
        #         element = '**' + element[:-4]
        #     elements.append(element)
        # return ''.join(elements)
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
            #     elements.append(element)
            # else:
            #     if len(element) < 18:
            #         elem = element[:6] + len(element[6:-4]) * '*' + element[-4:]
            #         elements.append(elem)
            #     else:
                element = '**' + element[-4:]
            elements.append(element)
        return ' '.join(elements)