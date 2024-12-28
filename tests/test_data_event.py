import unittest

from bms.commands import DataEventCommand
from tests.mock_serial_connection import MockSerialConnection


class TestDataEventCommand(unittest.TestCase):

    def setUp(self):
        self.serial = MockSerialConnection('data_event')

    def _get_test_class(self):
        return DataEventCommand(self.serial)

    def test___init__(self):
        de_command = self._get_test_class()
        assert de_command is not None

    def test__parse_header(self):
        de_command = self._get_test_class()
        output = de_command.get_last_event()
        assert output is not None