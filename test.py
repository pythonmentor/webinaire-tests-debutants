import io
import sys


class Terminal:
    def __init__(self):
        self._output = sys.stdout = io.StringIO()
        self._error = sys.stderr = io.StringIO()
        self._input = sys.stdin = io.StringIO()

    @property
    def input(self):
        return self._input.getvalue()

    @input.setter
    def input(self, value):
        self._input = sys.stdin = io.StringIO(str(value))

    @property
    def output(self):
        return self._output.getvalue()

    @property
    def error(self):
        return self._error.getvalue()