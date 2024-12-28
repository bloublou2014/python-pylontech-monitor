from bms.commands import DataEventCommand
from bms.serial_connector import SerialConnector
from bms.commands.power import PowerCommand
from bms.commands.batteries import BatteriesCommand


class BMSController:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.connection = SerialConnector(self.serial_port)

    def power(self):
        power_command = PowerCommand(self.connection)
        result = power_command.execute()
        return result

    def batteries(self):
        command = BatteriesCommand(self.connection)
        result = command.execute()
        return result

    def last_event(self):
        command = DataEventCommand(self.connection)
        result = command.get_last_event()
        return result

    def get_last_events(self, n=1):
        command = DataEventCommand(self.connection)
        result = command.get_last_events(n)
        return result
