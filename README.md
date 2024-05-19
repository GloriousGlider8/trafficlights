# trafficlights

A python library for preventing race conditions

[![Upload Python Package](https://github.com/GloriousGlider8/trafficlights/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/GloriousGlider8/trafficlights/actions/workflows/python-publish.yml)

## Classes

### Signal()

Signal with signal.wait()

```python
# This is inefficient and you should use
# k.wait("enter") instead.

import trafficlights as tl
import keyboard as k

signal = tl.Signal()

k.add_hotkey("enter", signal.set, args=(True,))

print("Waiting for [ENTER]")

signal.wait(True)
```

##### Functions

**Signal.set(val: bool) -> None:**

Sets signal.status to val.

**Signal.wait(val: bool) -> None:**

Waits for signal.status to be the same as val.

##### Properties

**Signal.status: bool**

The status of the signal. False for red, True for green.

### ThreadSignal() extends Signal()

ThreadSignal() with ThreadSignal.status

```python
import trafficlights as tl

def count():
    for i in range(10000): # Very slow operation, to be done in another thread.

signal = tl.ThreadSignal()
signal.tie(count)
signal.run()

print("Other operation...")
# Wait for the signal to turn green (completed)
while not signal.status:
    print("Still not!")
print("Done!")
```

ThreadSignal() with ThreadSignal.wait()

```python
import trafficlights as tl

def count():
    for i in range(10000): # Very slow operation, to be done in another thread.
        print(i)

signal = tl.ThreadSignal()
signal.tie(count)
signal.run()

print("Other operation...")
# Wait for the signal to turn green (completed)
signal.wait(True)
print("Done!")
```

##### Functions

**All Signal functions**

**ThreadSignal.tie(func: function) -> None:**

Tie a function to be run on ThreadSignal.run().

**ThreadSignal.run(args: tuple) -> None:**

Start the thread to run ThreadSignal._func().

**ThreadSignal._exec(args: tuple) -> None:**

Executed in a thread by ThreadSignal.run().

##### Properties

**All Signal Properties**

**ThreadSignal._func: function:**

Executed by ThreadSignal._exec(), set by ThreadSignal.tie().

### SignalError() extends BaseException()

An error.

```python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import trafficlights as tl

>>> signal = tl.ThreadSignal()
>>> # Did not tie a function to the ThreadSignal!
>>> signal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SignalError: No function tied.
```

### VarClass()

A class which can hold any value, useful for ThreadSignals which don't have access to standard variables

```python
import trafficlights as tl

var = tl.VarClass()

var.set(3 + 3)
print(var.get()) # 9
```

##### Functions

**VarClass.set(val: Any) -> None:**

Sets VarClass._val

**VarClass.get() -> Any:**

Returns VarClass._val

##### Properties

**VarClass._val: Any:**

The data stored inside the variable.
