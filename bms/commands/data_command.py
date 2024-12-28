from tkinter.constants import SEPARATOR

from bms.commands.base_command import BaseCommand
from _datetime import datetime
import re

SEPARATOR = '-----------------------------------------------'


class DataCommand(BaseCommand):
    _command_name = 'data'
    _int_names = ['item_index', 'rec_item_index', 'percent', 'battery', 'coulomb']
    _float_names = ['voltage', 'current', 'temperature', 'total_coulomb', 'max_voltage', 'volt', 'curr', 'tempr']
    _time_names = ['time']
    _multiple_values = ['bat_protect_ena', 'pwr_protect_ena']
    _is_array = False

    def __init__(self, serial_connection):
        self.serial_connection = serial_connection

    def _split_header_and_array(self, result):
        if not result:
            return None
        header = []
        array = []
        current = header
        index = 0
        for line in result:
            if line == SEPARATOR:
                index += 1
                current = array if index == 2 else header
                continue
            if line:
                current.append(line)
        return header, array

    def _parse_line(self, line):
        p = re.compile(r'^([^:]+)\s+:\s+(.+)\s*$', re.IGNORECASE)
        match = p.match(line)
        if match:
            return match.group(1), match.group(2)
        return None, None

    def _parse_header(self, header):
        if not header:
            return None
        p = re.compile(r'^([^:]+)\s+:\s+(.+)\s*$', re.IGNORECASE)
        output = {}
        for line in header:
            match = p.match(line)
            if not match:
                continue
            name = self._normalize_name(match.group(1))
            value = match.group(2).strip()
            if name not in self._multiple_values and name not in self._time_names:
                value = value.split(' ')[0]
            value = self._parse_value(name, value)
            output[name] = value
        return output

    def parse(self, result):
        if not result:
            return None
        # parse event
        header, array = self._split_header_and_array(result)
        header_values = self._parse_header(header)
        array_value = self._parse_array(array)

        return {
            'header': header_values,
            'array': array_value
        }

    def get_event(self, index):
        result = self.serial_connection.execute_command(f'{self._command_name} {index}')
        return self.parse(result)

    def get_last_event(self):
        result = self.serial_connection.execute_command(self._command_name)
        return self.parse(result)

    def get_events(self, from_index=None, to_index=None):
        if not from_index:
            from_index = 1
        if not to_index:
            to_index = self.nb_events()
        events = []
        for i in range(from_index, to_index):
            events.append(self.get_event(i))
        return events

    def get_last_events(self, n=1):
        to_index = self.nb_events()
        from_index = to_index - n + 1
        return self.get_events(from_index, to_index)

    def nb_events(self):
        result = self.get_last_event()
        return result['header']['item_index']
