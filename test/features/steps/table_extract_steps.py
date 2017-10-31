from behave import given, when, then
from nose.tools import assert_in

from pdftablr.table_extractor import Extractor
import sys


@given('I am using the Table Extractor')
def step_impl(context):
    context.extractor = Extractor(output_file=None)


@when(u'I am processing the file "{file}"')
def step_impl(context, file):
    with open(file) as f:
        context.extractor.read_file(f)

    tables = context.extractor.extract()
    context.result = sys.stdout

    for table in tables:
        table.output(writer=None)


@then(u'The output should match the contents of the file "{file}"')
def step_impl(context, file):
    with open(file) as f:
        expected_result = "".join(f.readlines())
    assert_in(expected_result, context.result.getvalue().replace('\r', '').replace(' \n', '\n'))
