from displacement import equation
from newton import solve

t_solution = solve()
displacement = equation(t_solution)

print(f"The displacement is {displacement:.2f} meters")
