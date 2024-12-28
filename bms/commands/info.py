from bms.commands.base_command import BaseCommand
import re
from datetime import datetime


# pylon>info
# info
# pylon>info
# @
# Device address      : 1
# Manufacturer        : Pylon
# Device name         : US2000C
# Board version       : V10R04
# Board               : NF4.E2
# Main Soft version   : B69.13.0.0
# Soft  version       : V1.4
# Boot  version       : V1.0
# Comm version        : V2.0
# Release Date        : 22-01-24
# Barcode             : K220803C30160910
#
# Specification       : 48V/50AH
# Cell Number         : 15
# Max Dischg Curr     : -90000mA
# Max Charge Curr     : 90000mA
# EPONPort rate       : 1200
# Console Port rate   : 115200
# Command completed successfully

ABSENT = ' -      Absent   -'


class PowerCommand(BaseCommand):
    _command_name = 'pwr'

    def _parse_value(self, name, value):
        if value == '-' or value == '':
            return None
        if name in ['volt', 'tempr', 'tlow', 'thigh', 'vlow', 'vhigh', 'mostempr']:
            return float('{}.{}'.format(value[:2], value[2:]))
        if name in ['power']:
            return int(value)
        if name == 'time':
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return value

    def parse(self, result):
        if not result:
            return None
        p = re.compile(r'\s+')
        headers = [x.lower().strip() for x in p.split(result[0])]
        output = []

        for line in result[1:]:
            content = p.split(line)
            content_len = len(content)
            if content_len > 14 and content[13] != '-':
                time_part = content.pop(14)
                content[13] += ' ' + time_part
            line_output = {}
            for i, header in enumerate(headers):
                if content_len <= i:
                    line_output[header] = None
                    continue
                line_output[header] = self._parse_value(header, content[i])
            output.append(line_output)
        return output
