def my_sum(x, y):
    """A function that sums. """
    return x+y

def my_mul(x, y):
    """A function that multiply. """
    return x*y

from sympy import symbols, Function, Eq, Derivative, dsolve, solve

def sistema(matriz):

    """Dada un lista de listas, regresa un sistema de ecuaciones diferenciales."""

    t = symbols('t')

    x, y = symbols('x y', cls=Function)

    eq1 = Eq(Derivative(x(t), t), matriz[0][0]*x(t) + matriz[0][1]*y(t))

    eq2 = Eq(Derivative(y(t), t), matriz[1][0]*x(t) + matriz[1][1]*y(t))

    sols = dsolve((eq1, eq2))

    return sols[0].rhs, sols[1].rhs


def saludo(persona):
    """A function that says hi to you."""
    return "¡Hola, " + persona 
