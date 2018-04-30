from unittest import TestCase
from main.processor import Processor


class TestProcessor(TestCase):

    def setUp(self):
        self.processor = Processor(csv_file='/csv_file/1.csv')

    def tearDown(self):
        del self.processor

    def test_process(self):
        self.fail()

    def test_flatten_row(self):
        self.fail()
