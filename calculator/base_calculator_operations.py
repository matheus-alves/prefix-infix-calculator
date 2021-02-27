"""
Helper module for converting the operator symbols to the built-in Python operators
"""

import operator as op

OPERATIONS = {
    '+': op.add,
    '*': op.mul,
    '/': op.truediv,
    '-': op.sub
}
