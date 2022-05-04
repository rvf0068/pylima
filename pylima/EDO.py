from sympy import symbols, Function, Eq, Derivative, dsolve

def cuadrados_fibonacci(n):
    fibs = []
    a, b = 0, 1
    while a < n:
        fibs.append(a)
        a, b = b, a+b
    return fibs


def sistema(matriz):
    """Dada un lista de listas, regresa un sistema de ecuaciones diferenciales."""
    t = symbols('t')
    x, y = symbols('x y', cls=Function)
    eq1 = Eq(Derivative(x(t), t), matriz[0][0]*x(t) + matriz[0][1]*y(t))
    eq2 = Eq(Derivative(y(t), t), matriz[1][0]*x(t) + matriz[1][1]*y(t))
    sols = dsolve((eq1, eq2))
    return sols[0].rhs, sols[1].rhs
