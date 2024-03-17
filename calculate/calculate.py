from .displacement import equation
from .newton import solve

def displacement():
    t_solution = solve()
    displacement = equation(t_solution)
    print(f"The displacement is {displacement:.2f} meters")
    print(f"The time of flight is {t_solution:.2f} seconds")
    return displacement, t_solution

if __name__ == "__main__":
    displacement()
