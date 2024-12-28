import unittest
from datetime import datetime

from bms.commands import BaseCommand
from bms.commands.batteries import BatteriesCommand
from tests.mock_serial_connection import MockSerialConnection


class TestBaseCommand(unittest.TestCase):

    def _get_test_class(self):
        base = BaseCommand(None)
        base._int_names = ['a', 'b']
        base._float_names = ['c', 'd', 'c.d']
        base._time_names = ['e']
        return base

    def test___init__(self):
        base_command = self._get_test_class()
        assert base_command is not None

    def test__parse_value(self):
        base_command = self._get_test_class()
        name = 'name'
        value = 'value'
        result = base_command._parse_value(name, value)
        assert result is not None

    def test__parse_value_float(self):
        base_command = self._get_test_class()
        names = ['c', 'd']
        value = '12345'
        for name in names:
            result = base_command._parse_value(name, value)
            assert result == 12.345

    def test__parse_value_int(self):
        base_command = self._get_test_class()
        names = ['a', 'b']
        value = '12345'
        for name in names:
            result = base_command._parse_value(name, value)
            assert result == 12345

    def test__parse_value_time(self):
        base_command = self._get_test_class()
        names = ['e']
        value = '2024-12-20 16:50:39'
        for name in names:
            result = base_command._parse_value(name, value)
            assert result == datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

    def test__parse_value_empty(self):
        base_command = self._get_test_class()
        name = 'name'
        values = ['-', '', ' ']
        for value in values:
            result = base_command._parse_value(name, value)
            assert result is None

    def test__parse_array_header(self):
        base_command = self._get_test_class()
        content = 'a v. State c.d time a.b Base State'
        result = base_command._parse_array_headers(content)
        assert result is not None
        assert len(result) == 6
        assert result[0] == 'a'
        assert result[1] == 'v_state'
        assert result[2] == 'c_d'
        assert result[3] == 'time'
        assert result[4] == 'a_b'
        assert result[5] == 'base_state'

    def test__parse_array(self):
        base_command = self._get_test_class()
        content = [
            'a v. State c.d time a.b.c',
            '0 blop 12345 2024-12-24 16:30:50'
        ]
        result = base_command._parse_array(content)
        assert result is not None
        assert len(result) == 1
        assert result[0] == {
            'a': 0,
            'v_state': 'blop',
            'c_d': 12.345,
            'time': datetime.strptime('2024-12-24 16:30:50', '%Y-%m-%d %H:%M:%S'),
            'a_b_c': None
        }
