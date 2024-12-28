import unittest

from bms.commands.batteries import BatteriesCommand
from tests.mock_serial_connection import MockSerialConnection


class TestBatteriesCommand(unittest.TestCase):

    def setUp(self):
        self.serial = MockSerialConnection('batteries')

    def _get_test_class(self):
        return BatteriesCommand(self.serial)

    def test___init__(self):
        batteries_command = self._get_test_class()
        assert batteries_command is not None

    def test__parse_value(self):
        batteries_command = self._get_test_class()
        name = 'name'
        value = 'value'
        result = batteries_command._parse_value(name, value)
        assert result is not None

    def test__parse_value_float(self):
        batteries_command = self._get_test_class()
        names = ['tempr', 'volt', 'coulomb']
        value = '12345'
        for name in names:
            result = batteries_command._parse_value(name, value)
            assert result == 12.345

    def test__parse_value_int(self):
        batteries_command = self._get_test_class()
        names = ['soc', 'battery']
        value = '12345'
        for name in names:
            result = batteries_command._parse_value(name, value)
            assert result == 12345
