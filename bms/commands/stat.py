from bms.commands.base_command import BaseCommand
import re
from datetime import datetime

# $$stat
# stat
# pylon>stat
# @
# Device address           1
# Data Items      :      233
# HisData Items   :     1793
# Charge Cnt.     :        0
# Discharge Cnt.  :        0
# Charge Times    :    49820
# Status Cnt.     :     4882
# Idle Times      :    54607
# COC Times       :        0
# COC2 Times      :        0
# DOC Times       :        0
# DOC2 Times      :        0
# COCA Times      :        0
# DOCA Times      :        0
# SC Times        :        4
# Bat OV Times    :        5
# Bat HV Times    :      209
# Bat LV Times    :        3
# Bat UV Times    :        0
# Bat SLP Times   :        0
# Pwr OV Times    :        0
# Pwr HV Times    :        0
# Pwr LV Times    :        6
# Pwr UV Times    :        0
# Pwr SLP Times   :        0
# COT Times       :        0
# CUT Times       :        0
# DOT Times       :        0
# DUT Times       :        0
# CHT Times       :        0
# CLT Times       :        0
# DHT Times       :        0
# DLT Times       :        0
# Shut Times      :        6
# Reset Times     :       42
# RV Times        :        0
# Input OV Times  :        0
# SOH Times       :      310
# BMICERR Times   :        0
# CYCLE Times     :      174
# SOH             :       99
# Pwr Percent     :       53
# Pwr Coulomb     : 93589924
# Dsg Cap         :  8732765
# HT@0.5C Cnt     :        0
# LT@0.5C Cnt     :        0
# HT Cnt          :        0
# LT Cnt          :        0
# LV Cnt          :      559
# LifeWarn Times  :        0
# LifeAlarm Times :        0
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
