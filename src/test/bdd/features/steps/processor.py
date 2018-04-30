from behave import *
from main.processor import Processor
import logging

logger = logging.getLogger('BDD Tester')

@step('I provide Processor with a file name {file_name}')
def step_impl(context, file_name):
    assert(file_name)
    processor = Processor(csv_file=file_name)
    context.processor = processor
    logger.info('Success: File Processor is created')

@step('I provide Processor with a directory name {dir_name}')
def step_impl(context, dir_name):
    assert(dir_name)
    processor = Processor(csv_dir=dir_name)
    context.processor = processor
    logger.info('Success: Dir Processor is created')

@step('I run the process')
def step_impl(context):
    result = context.processor.process()
    assert(result)
    context.result = result
    logger.info('Success: process executed')

@step('I receive the result list of length {length}')
def step_impl(context, length):
    result = context.result
    assert(len(result) == int(length))
    logger.info('Success: result length {} is verified'.format(length))