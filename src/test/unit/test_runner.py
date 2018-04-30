import unittest
from main.processor import Processor
from main.record import Record
import logging

class TestRunner(unittest.TestCase):

    logger = logging.getLogger('TestRunner')

    def setUp(self):
        self.file_processor = Processor(csv_file='../csv_files/1.csv')
        self.dir_processor = Processor(csv_dir='../csv_files')

    def tearDown(self):
        del self.file_processor

    def test_process(self):
        file_result = self.file_processor.process()
        assert(file_result)
        assert(len(file_result) == 2)
        self.logger.info('Success: file processor is tested')

        dir_result = self.dir_processor.process()
        assert(dir_result)
        assert(len(dir_result) == 6)
        self.logger.info('Success: dir processor is tested')

    def test_flatten_row(self):
        row = {'mon-wed': 5, 'thu-fri': 8}
        result = self.file_processor.flatten_row(row)
        assert(result)
        assert(result['mon'] == 5)
        assert(result['tue'] == 5)
        assert(result['wed'] == 5)
        assert(result['thu'] == 8)
        assert(result['fri'] == 8)
        self.logger.info('Success: flattening is tested')


if __name__ == '__main__':
    unittest.main()