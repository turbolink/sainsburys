from main.processor import Processor
import os

if __name__ == '__main__':
    '''
    Runs Processor with one parameter - either CSV file or CSV directory.
    '''
    proc = Processor(csv_dir='../csv_files/')
    # proc = Processor(csv_file='../csv_files/1.csv')
    result = proc.process()
    for i in result:
        print(i)