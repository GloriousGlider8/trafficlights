import typing as _typ
from time import sleep as _wait
import threading as _t

_thrNo = 0

class VarClass():
    def set(self, val: _typ.Any) -> None:
        self._val = val
    def get(self) -> _typ.Any:
        return self._val

class SignalError(BaseException):
    pass

class Signal():
    def __init__(self) -> None:
        self.status = False
    def set(self, val: bool) -> None:
        self.status = val
    def wait(self, val: bool) -> None:
        while self.status != val:
            _wait(0.1)

class ThreadSignal(Signal):
    def __init__(self):
        self._func = None
        self.status = False
    def tie(self, func: function) -> None:
        self._func = func
    def run(self, args: tuple) -> None:
        global _thrNo
        _thrNo += 1
        _t.Thread(target=self._exec, name="ThreadSignal" + str(_thrNo), args=args)
    def _exec(self, args) -> None:
        self.set(False)
        if not self._func:
            raise SignalError("No function tied.")
        try:
            self._func(args)
        except Exception as e:
            self.set(True)
            raise SignalError("Error in " + _t.current_thread().name + " (" + ", ".join(e.args) + ")")
        self.set(True)