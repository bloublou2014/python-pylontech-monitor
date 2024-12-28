from _datetime import datetime
import re


class BaseCommand:
    _command_name = ''
    _int_names = []
    _float_names = []
    _time_names = []
    _multiple_values = []
    _is_array = False

    def __init__(self, serial_connection):
        self.serial_connection = serial_connection

    # region Parse array
    def _parse_array(self, result):
        if not result:
            return None
        headers = self._parse_array_headers(result[0])
        return self._parse_array_content(result[1:], headers)

    def _normalize_name(self, name):
        return re.sub(r'[._\s]+', '_', name.lower().strip())

    def _parse_array_headers(self, line):
        if not line:
            raise ValueError('Line is empty')
        p = re.compile(r'([a-z0-9]+(\.\s?[a-z]+|\sState)?)', re.IGNORECASE)
        headers = [self._normalize_name(x[0]) for x in p.findall(line)]
        return headers

    def _parse_array_content(self, lines, headers):
        if not lines:
            raise ValueError('Line is empty')
        output = []
        p_line = re.compile(r'(([-a-z0-9]+(\s[0-9]+:[0-9]+:[0-9]+)?)(%|\smAH)?)', re.IGNORECASE)
        for line in lines:
            content = [x[1] for x in p_line.findall(line)]
            content_len = len(content)
            line_output = {}
            for i, header in enumerate(headers):
                if content_len <= i:
                    line_output[header] = None
                    continue
                line_output[header] = self._parse_value(header, content[i])
            output.append(line_output)
        return output

    # endregion

    def _parse_value(self, name, value):
        if not value or value == '-' or value.strip() == '':
            return None
        if name in self._float_names:
            if len(value) > 2:
                return float('{}.{}'.format(value[:2], value[2:]))
            return float(value)
        if name in self._int_names:
            return int(value)
        if name in self._time_names:
            return datetime.strptime(value, '%y-%m-%d %H:%M:%S' if len(value) == 17 else '%Y-%m-%d %H:%M:%S')
        if name in self._multiple_values:
            return value.split()
        return value

    def parse(self, result):
        if self._is_array:
            return self._parse_array(result)
        return None

    def execute(self):
        result = self.serial_connection.execute_command(self._command_name)
        return self.parse(result)
