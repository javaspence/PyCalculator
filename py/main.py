print('PyCalculator v0.2-alpha (Mark I)')
print('Developed by Spencer Roudebush')
import pycalc
from pycalc import number1, number2, method
import math


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
