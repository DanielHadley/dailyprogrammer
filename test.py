
"""Roots of a polynomial"""
import re
import sys

Input = 'x^4-2x^3+7x^2-16x+4'

# Turn the string into a function that Python can evaluate
def TurnInputToFunction(Input):
    function = Input.replace('^', '**').replace('x', '*x')
    if function.startswith('*'):
        function = function[1:]
    return function

def f(x):
    x = x
    return eval(TurnInputToFunction(Input))


def secant(x0,x1,sims):
    for i in range(sims):
        if f(x1)-f(x0) == 0:
            return x1
        x_temp = x1 - (f(x1)*(x1-x0)*1.0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x_temp
    return x1
    

print secant(10, 30, 20)
