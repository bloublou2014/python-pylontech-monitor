import serial
import time

PYLON_COMMAND_LINE = ['pylon_debug>', 'pylon>', '$$', '@']
PYLON_COMMAND_COMPLETED = ['Command completed successfully']


class SerialConnector:
    def __init__(self, serial_port, serial_connection=None):
        self.serial_port = serial_port
        self.serial_connection = serial_connection

    def serial_open(self, baud):
        ser = serial.Serial(port=self.serial_port,
                            baudrate=baud,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=10
                            )
        if ser.portstr:
            print('...connected to: ' + ser.portstr)
        self.serial_connection = ser

    def serial_write_init(self):
        packet = bytearray()
        packet.append(0x7E)
        packet.append(0x32)
        packet.append(0x30)
        packet.append(0x30)
        packet.append(0x31)
        packet.append(0x34)
        packet.append(0x36)
        packet.append(0x38)
        packet.append(0x32)
        packet.append(0x43)
        packet.append(0x30)
        packet.append(0x30)
        packet.append(0x34)
        packet.append(0x38)
        packet.append(0x35)
        packet.append(0x32)
        packet.append(0x30)
        packet.append(0x46)
        packet.append(0x43)
        packet.append(0x43)
        packet.append(0x33)
        packet.append(0x0D)
        self.serial_connection.write(packet)

    def serial_write_open_console(self):
        packet = bytearray()
        packet.append(0x0D)
        packet.append(0x0A)
        self.serial_connection.write(packet)

    def connect(self):
        self.serial_open(1200)
        self.serial_write_init()
        self.serial_connection.close()
        self.serial_open(115200)
        self.serial_write_open_console()

    def disconnect(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
        self.serial_connection = None

    def _read_line(self):
        read_serial = self.serial_connection.readline()
        # print(read_serial)
        if read_serial:
            read_serial = read_serial.decode('ascii')
        return read_serial

    def _get_clean_prompt(self):
        self.serial_connection.write('\r'.encode())
        while True:
            read_serial = self._read_line()
            if read_serial:
                if read_serial.strip() in PYLON_COMMAND_LINE:
                    break

    def _cleanup_result(self, result):
        output = []
        for line in result.split('\r'):
            line = line.strip()
            if not line or line in PYLON_COMMAND_COMPLETED or line in PYLON_COMMAND_LINE:
                continue
            output.append(line)
        return output

    def execute_command(self, command: str):
        if not command:
            raise ValueError('Command is empty')
        if not self.serial_connection:
            self.connect()
        self._get_clean_prompt()
        self.serial_connection.write((command + '\r').encode())
        cache = ''
        while True:
            read_serial = self._read_line()
            if read_serial:
                stripped = read_serial.strip()
                if stripped in PYLON_COMMAND_LINE or stripped.startswith('pylon>') or stripped.startswith('pylon_debug>'):
                    continue
                if stripped in PYLON_COMMAND_COMPLETED:
                    return self._cleanup_result(cache)
                cache += read_serial
