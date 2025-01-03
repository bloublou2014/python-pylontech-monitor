from bms.commands.base_command import BaseCommand
import re
from datetime import datetime

# $$data event
# data event
# pylon>data event
# @
# -----------------------------------------------
# Item Index      : 232
# Time            : 24-12-09 16:53:35
# Voltage         : 49958       mV
# Current         : 0           mA
# Temperature     : 15000       mC
# Percent         : 18          %
# Total Coulomb   : 50000       mAH
# Max Voltage     : 54000       mV
# Base State      : SysError
# Volt. State     : Normal
# Curr. State     : Normal
# Tempr. State    : Normal
# Coul. Status    : Low
# Power Events    : 0x0
# Bat Events      : 0x2        BHV
# Bat Protect ENA : BOV BHV BLV BUV BSLP CBOT CBHT CBLT CBUT DBOT DBHT DBLT DBUT
# Pwr Protect ENA : POV PHV PLV PUV PSLP POT PHT COC2 COC COCA DOCA DOC DOC2 SC LCOUL
# System Fault    : 0x8
# -----------------------------------------------
#
# Battery  Volt     Curr     Tempr    Base State   Volt. State  Curr. State  Temp. State  Coulomb
# 0        3275     0        10600    Idle         Normal       Normal       Normal       18%
# 1        3277     0        10600    Idle         Normal       Normal       Normal       18%
# 2        3274     0        10600    Idle         Normal       Normal       Normal       18%
# 3        3276     0        10600    Idle         Normal       Normal       Normal       18%
# 4        3278     0        10600    Idle         Normal       Normal       Normal       18%
# 5        3274     0        10800    Idle         Normal       Normal       Normal       18%
# 6        3275     0        10800    Idle         Normal       Normal       Normal       18%
# 7        3276     0        10800    Idle         Normal       Normal       Normal       18%
# 8        3278     0        10800    Idle         Normal       Normal       Normal       18%
# 9        3276     0        10800    Idle         Normal       Normal       Normal       18%
# 10       3276     0        10500    Idle         Normal       Normal       Normal       18%
# 11       3276     0        10500    Idle         Normal       Normal       Normal       18%
# 12       3277     0        10500    Idle         Normal       Normal       Normal       18%
# 13       4095     0        10500    Idle         High         Normal       Normal       19%
# 14       3275     0        10500    Idle         Normal       Normal       Normal       18%
# Command completed successfully
# $$data history
# data history
# pylon>datahistory
# @
# -----------------------------------------------
# Rec Item Index  : 1799
# Time            : 24-12-26 13:50:30
# Voltage         : 49397       mV
# Current         : 0           mA
# Temperature     : 21800       mC
# Percent         : 53          %
# Total Coulomb   : 50000       mAH
# Max Voltage     : 54000       mV
# Base State      : Idle
# Volt. State     : Normal
# Curr. State     : Normal
# Tempr. State    : Normal
# Coul. Status    : Normal
# Power Events    : 0x0
# Bat Events      : 0x0
# Bat Protect ENA : BOV BHV BLV BUV BSLP CBOT CBHT CBLT CBUT DBOT DBHT DBLT DBUT
# Pwr Protect ENA : POV PHV PLV PUV PSLP POT PHT COC2 COC COCA DOCA DOC DOC2 SC LCOUL
# System Fault    : 0x0
# -----------------------------------------------
#
# Battery  Volt     Curr     Tempr    Base State   Volt. State  Curr. State  Temp. State  Coulomb
# 0        3293     0        19200    Idle         Normal       Normal       Normal       53%
# 1        3293     0        19200    Idle         Normal       Normal       Normal       53%
# 2        3293     0        19200    Idle         Normal       Normal       Normal       53%
# 3        3293     0        19200    Idle         Normal       Normal       Normal       53%
# 4        3294     0        19200    Idle         Normal       Normal       Normal       53%
# 5        3293     0        19300    Idle         Normal       Normal       Normal       53%
# 6        3293     0        19300    Idle         Normal       Normal       Normal       53%
# 7        3293     0        19300    Idle         Normal       Normal       Normal       53%
# 8        3294     0        19300    Idle         Normal       Normal       Normal       53%
# 9        3293     0        19300    Idle         Normal       Normal       Normal       53%
# 10       3293     0        19100    Idle         Normal       Normal       Normal       53%
# 11       3293     0        19100    Idle         Normal       Normal       Normal       53%
# 12       3293     0        19100    Idle         Normal       Normal       Normal       53%
# 13       3293     0        19100    Idle         Normal       Normal       Normal       53%
# 14       3293     0        19100    Idle         Normal       Normal       Normal       53%
# Command completed successfully


class EventsCommand(BaseCommand):
    _command_name = 'data event'

