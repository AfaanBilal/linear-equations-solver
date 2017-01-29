# ------------------------------------------
#  Linear Equations Solver
#  Author: Afaan Bilal
#  URL: https://afaan.ml
# ------------------------------------------

from sympy import Matrix, S, linsolve, symbols

print("Linear Equations Solver")
print("(c) Afaan Bilal (https://afaan.ml)")
print("-----------------------------------")

n = int(input("Enter the number of variables: "))
print()

xs = []
for i in range(1, n + 1):
    x = symbols("x" + str(i))
    xs.append(x)

Coeffs = []
Consts = []
for i in range(1, n + 1):
    cfs = []
    for j in range(1, n + 1):
        c = float(input("Enter coefficient " + str(j) + " of equation " + str(i) + ": "))
        cfs.append(c)
    c = float(input("Enter the constant  of equation " + str(i) + ": "))
    Coeffs.append(cfs)
    Consts.append(c)
    print()

A = Matrix(Coeffs)
b = Matrix(Consts)

soln = linsolve((A, b), xs)
print("\nSolutions:")
for i in soln:
    print(i)
