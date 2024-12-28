from bms.commands.base_command import BaseCommand


# Power Volt   Curr   Tempr  Tlow   Thigh  Vlow   Vhigh  Base.St  Volt.St  Curr.St  Temp.St  Coulomb  Time                 B.V.St   B.T.St   MosTempr M.T.St
# 1     49426  0      18900  19000  19200  3295   3296   Idle     Normal   Normal   Normal   53%      2024-12-26 11:50:39  Normal   Normal  18900    Normal
# 2     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 3     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 4     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 5     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 6     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 7     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 8     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 9     -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 10    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 11    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 12    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 13    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 14    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 15    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# 16    -      -      -      -      -      -      -      Absent   -        -        -        -        -                    -        -
# Command completed successfully

class PowerCommand(BaseCommand):
    _command_name = 'pwr'
    _int_names = ['power', 'coulomb']
    _float_names = ['volt', 'tempr', 'curr', 'tlow', 'thigh', 'vlow', 'vhigh', 'mostempr']
    _time_names = ['time']
    _is_array = True
