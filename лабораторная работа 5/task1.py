# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
keys = ['bin', 'dec', 'hex', 'oct']
dict = [{'bin': bin(i), 'dec': (i), 'hex': hex(i), 'oct': oct(i),}  for i in range(16)]
pprint(dict)
