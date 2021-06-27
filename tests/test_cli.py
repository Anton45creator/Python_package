from src.cli import cli
from unittest import mock
import argparse


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(file=["hello"], text=None))
def test_parsing_file(mock_args):
    result = cli.cli()
    assert result == "file: 3"


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(file=['random', 'character',
                                                  'set'], text=None))
def test_parsing_file_3_lines(mock_args):
    result = cli.cli()
    assert result == 'file: 6 3 3'


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(text='hello', file=None))
def test_parsing_string(mock_args):
    result = cli.cli()
    assert result == 'text: 3'


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(file=['tested'], text='value'))
def test_parsing_file_and_string(mock_args):
    result = cli.cli()
    assert result == 'file: 2 text: 5'