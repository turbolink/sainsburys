from collections import OrderedDict
import json

class Record:
    '''
    Record is a data holder of an individual row
    that contains data values for one day.
    It provides labels 'square' or 'double' for days
    given in corresponding lists.
    '''

    days_square = ['mon', 'tue', 'wed']
    days_double = ['thu', 'fri']

    def __init__(self, day, desc, value):
        '''
        Assigns values to corresponding fields.
        :param day:
        :param desc:
        :param value:
        '''
        self.day = day
        self.value = value
        if self.day in self.days_square:
            self.factor = 'square'
            self.factor_num = value**2
        elif self.day in self.days_double:
            self.factor = 'double'
            self.factor_num = value * 2
        else:
            raise Exception('Unrecognised day...')
        self.desc = '{} {}'.format(desc, self.factor_num)

    def __str__(self):
        '''
        Provids JSON formated string for self-representation.
        :return:
        '''
        return json.dumps(OrderedDict([
            ('day', self.day),
            ('descrition', self.desc),
            (self.factor, self.factor_num),
            ('value', self.value)
        ]), separators=(', ', ': '))
