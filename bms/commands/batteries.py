from bms.commands.base_command import BaseCommand
import re
from datetime import datetime


# bat
# @
# Battery  Volt     Curr     Tempr    Base State   Volt. State  Curr. State  Temp. State  SOC          Coulomb      BAL
# 0        3293     0        19200    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 1        3293     0        19200    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 2        3293     0        19200    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 3        3293     0        19200    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 4        3294     0        19200    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 5        3293     0        19300    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 6        3292     0        19300    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 7        3293     0        19300    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 8        3294     0        19300    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 9        3293     0        19300    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 10       3293     0        19100    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 11       3293     0        19100    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 12       3293     0        19100    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 13       3293     0        19100    Idle         Normal       Normal       Normal       53%         26015 mAH      N
# 14       3293     0        19100    Idle         Normal       Normal       Normal       53%         26015 mAH      N

# bat 1 0
# pylon>bat 1 0
# @
# ----------------------------
# Power  1  Battery  0
#
# Volt Status : Normal
# Tmpr. Status: Normal
# Voltage     : 3293    mV
# Current     : 0       mA
# Temperature : 19200   mC 2923    0.1K
# ----------------------------
# Command completed successfully


class BatteriesCommand(BaseCommand):
    _command_name = 'bat'
    _int_names = ['soc', 'battery']
    _float_names = ['volt', 'tempr', 'coulomb', 'curr']
    _is_array = True
