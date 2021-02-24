#the only reason this is python 2.7 is because they didn't add support for str(input()) in python 3
print('PyCalculator v0.2-alpha (Mark I)')
print('Developed by Spencer Roudebush')
import pycalc
from pycalc import number1, number2, method

if method == str('add'):
  method_is_two = bool('false')
  print(number1 + number2)
  reload(pycalc)
