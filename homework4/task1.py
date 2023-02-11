"""
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""


def calc_pi(eps=1.0e-4):
    sum = 0
    d = 1
    sgn = 1
    while True:
        a = 4 / d
        sum = sum + sgn * a
        if a < eps:
            return sum
        sgn = -sgn
        d = d + 2


print(calc_pi())
