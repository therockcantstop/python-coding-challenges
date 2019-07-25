# Can import an operation and compute that equation 

import operator

def get_truth(inp, relate, cut):
    ops = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne
    }
    return ops[relate](inp, cut)

