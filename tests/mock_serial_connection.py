from os import path


class MockSerialConnection(object):
    def __init__(self, filename: str):
        self.response = self._read_file_content(filename).split('\n')

    def _read_file_content(self, filename: str):
        abs_path = path.join(path.dirname(path.abspath(__file__)), 'data', filename + '.txt')
        with open(abs_path, 'r') as file:
            return file.read()

    def execute_command(self, command: str):
        return self.response
