from scipy.optimize import root
import numpy as np

def equations(vars):

    Q1, Q2, Q3, Q4, Q5, Q6, Q7 = vars

    # Continuity equations

    eq1 = Q1 + Q6 - 2.5
    eq2 = Q1 - Q2 - Q7
    eq3 = Q2 - Q3 - 0.5
    eq4 = Q3 + Q4 - 1
    eq5 = -Q4 + Q5 - 1
    eq6 = Q6 - Q5
    eq7 = Q1**2 + (32.552*(Q7**2)) - (12.86 * (Q5**2)) - (1.017*(Q6**2))

    return np.array([eq1, eq2, eq3, eq4, eq5, eq6, eq7])

def jacobian(vars):
    Q1, Q2, Q3, Q4, Q5, Q6, Q7 = vars
    # Compute the Jacobian matrix
    J = np.array([
        [1, 0, 0, 0, 0, 1, 0],  # Fill in the derivatives of eq1 with respect to x1, x2, ..., x7
        [1, -1, 0, 0, 0, 0, -1],  # Derivatives of eq2
        [0, 1, -1, 0, 0, 0, 0],  # Derivatives of eq3
        [0, 0, 1, 1, 0, 0, 0],  # Derivatives of eq4
        [0, 0, 0, -1, 1, 0, 0],  # Derivatives of eq5
        [0, 0, 0, 0, -1, 1, 0],  # Derivatives of eq6
        [2*Q1, 0, 0, 0, 25.72*Q5, 2.214*Q6, 65.104*Q7]   # Derivatives of eq7
    ])
    return J

def d_w(L, D, Q):

    h_f = (8 * friction_factor * L * Q**2) / ((np.pi)**2 * g * D**5)

    return h_f

# Initial guess for the variables
initial_guess = [0] * 7  # Adjust initial values as needed

# Find the solution
solution = root(equations, initial_guess, jac=jacobian)

if solution.success:
    ans = solution.x

    for i in range(len(ans)) : # Truncating to 2 Decimal Places
        ans[i] = round(ans[i], 2)

    Q1, Q2, Q3, Q4, Q5, Q6, Q7 = ans

    print("Flow rates (m³/s):")
    print("Q1 =", Q1)
    print("Q2 =", Q2)
    print("Q3 =", Q3)
    print("Q4 =", Q4)
    print("Q5 =", Q5)
    print("Q6 =", Q6)
    print("Q7 =", Q7)

    # Pipe properties (in m)
    pipes = [
        {'length': 600, 'diameter': 0.25},
        {'length': 600, 'diameter': 0.15},
        {'length': 200, 'diameter': 0.1},
        {'length': 600, 'diameter': 0.15},
        {'length': 600, 'diameter': 0.15},
        {'length': 200, 'diameter': 0.2},
        {'length': 200, 'diameter': 0.1}
    ]

    friction_factor = 0.2
    g = 9.81

    h_A = 15
    h_B = h_A - d_w(pipes[0]["length"], pipes[0]["diameter"], Q1)
    h_C = h_B - d_w(pipes[1]["length"], pipes[1]["diameter"], Q2)
    h_D = h_C - d_w(pipes[2]["length"], pipes[2]["diameter"], Q3)
    h_E = h_D - d_w(pipes[3]["length"], pipes[3]["diameter"], Q4)
    h_F = h_E - d_w(pipes[4]["length"], pipes[4]["diameter"], Q5)

    print("\nHeads at nodes (m):")
    print("h_A =", h_A)
    print("h_B =", h_B)
    print("h_C =", h_C)
    print("h_D =", h_D)
    print("h_E =", h_E)
    print("h_F =", h_F)

else:
    print("No solution found.")
