from equation.quadratic_equation import QuadraticEquation

print(" X**2 + X + C = eq")
print("===============================")

QuadraticEquation(1, 5, 6, 0).solve()

print("------------------------------")

QuadraticEquation(1, -5, -6, 0).solve()
print("------------------------------")

try:
    QuadraticEquation(0, 0, 0, 0).solve()
except Exception as e:
    print(e)

print("------------------------------")

QuadraticEquation(5, 2, 1, 0).solve()

