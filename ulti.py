# -*- coding: utf-8 -*-

try: # Python 3.x
  from itertools import zip
except ImportError: # Python 2.x
  from itertools import izip as zip

from itertools import chain, repeat

def iterable_to_chunks(iterable, size, fill=None):
  '''Split a list to chunks

    iterable : an iterable object, e.g. generator, list, array, etc.
    size : chunk size, positive integer
    fill : padding values.

    Example :

      tochunks('abcdefg', 3, 'x')

    Output :

      ('a','b','c'), ('d','e','f'), ('g','x','x')

    reference :

      http://stackoverflow.com/a/312644

  '''
  return zip(*[chain(iterable, repeat(fill, size-1))]*size)

if __name__ == '__main__' :

  seq = [i for i in xrange(10)]
  it = xrange(10)
  print [i for i in iterable_to_chunks(it, 3, 9)]
  print [i for i in iterable_to_chunks(seq, 3, 9)]
