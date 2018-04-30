import logging
from record import Record
import csv, os

class Processor:
    '''
    Processor retrieves data from given CSV file/s and builds
    a list of strings that are compliant with given requirements.
    '''

    logger = logging.getLogger('Processor')
    week_days = ['mon', 'tue', 'wed', 'thu', 'fri']

    def __init__(self, csv_file=None, csv_dir=None):
        '''
        Constructor validates names given for CSV file or CSV directory
        given as input parameters. Parameters are self-exclusive, only
        one parameter should be specified.
        :param csv_file: string
        :param csv_dir: string
        '''
        error_msg = 'Please, provide either csv_file or csv_dir'

        # validate input parameters
        if csv_file and csv_dir:
            self.logger.error(error_msg)
            exit(-1)

        # validate CSV file
        if csv_file:
            if not (os.path.exists(csv_file) and os.path.isfile(csv_file)):
                raise Exception('Invalid CSV file name: {}'.format(csv_file))
            self.csv_files = [csv_file]

        # validate CSV directory
        elif csv_dir:
            self.csv_files = [f for f in os.listdir(csv_dir) if os.path.isfile(os.path.join(csv_dir, f)) and f[-3:].lower() == 'csv']
            if not self.csv_files:
                raise Exception('Failed to find any CSV file in {}'.format(csv_dir))
            self.csv_files = map(lambda f : os.path.join(csv_dir, f), self.csv_files)

        # stop the program if parameters are not provided
        else:
            self.logger.error(error_msg)
            exit(-1)


    def process(self):
        '''
        Retrives data from given CSV file/s and
        constructs a list of output string/s.
        :return: list of strings
        '''
        result = []
        for csv_file in self.csv_files:
            records = []
            with open(csv_file) as f:
                reader = csv.DictReader(f)
                row = next(reader)
                flat_row = self.flatten_row(row)

                for day in self.week_days:
                    desc = flat_row.get('description')
                    value = flat_row.get(day)
                    record = Record(day=day, desc=desc, value=int(value))
                    records.append(str(record))

            # format list of output strings
            # add CSV file name
            result.append(csv_file[csv_file.rfind('/') + 1:])
            # add records found in the CSV file
            result.append('[{}]\n'.format(',\n '.join(records)))
        return result

    def flatten_row(self, row):
        '''
        Flattens/expands a table given in CSV file - converts columns,
        like mon-thu, into multiple columns with individual values.
        :param row: dict
        :return: dict
        '''
        result = {}
        for key in row.keys():
            if '-' in key:
                days = key.split('-')
                subset = self.week_days[self.week_days.index(days[0]):self.week_days.index(days[1])+1]
                for day in subset:
                    result[day] = row[key]
            else:
                result[key] = row[key]
        return result