import pycalc
from pycalc import number1, number2, method
import math
import os
import sys


if method == str('add'):
  print(number1 + number2)

if method == str('subtract'):
  print(number1 - number2)

if method == str('multiply'):
  print(number1 * number2)

if method == str('divide'):
  print(number1 / number2)

if method == str('square root'):
  print(math.sqrt(number1))

os.execv(sys.executable, ['python'] + sys.argv)
