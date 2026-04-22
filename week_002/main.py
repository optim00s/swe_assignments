import numpy as np

def solve_system():
    # Define the 7x7 coefficient matrix A
    A = np.array([
        [ 2, -7,  3,  5, -7, 11,  8],
        [ 5,  7, -1,  9, -6,  3, -5],
        [13, 11,  8,  7,  4,  2,  1],
        [12,  1,  6,  5,  9,  3, 11],
        [ 1, -4,  7, -3,  9, -2,  6],
        [ 4,  1, -6, -3,  8, -7, -4],
        [-7, -2,  5,  1,  9,  3, -4]
    ])
    
    # Define the 7x1 constants vector b
    b = np.array([114, -11, -25, -37, 4, -91, -50])
    
    # Solve the system
    # A try-except block to handle cases where the system has no unique solution
    try:
        X = np.linalg.solve(A, b)
        
        # Format and print the output
        variables = ['s', 't', 'u', 'v', 'w', 'x', 'y']
        print("--- Solution Found ---")
        for var, val in zip(variables, X):
            # Using .4f to round to 4 decimal places for readability
            print(f"{var} = {val:.4f}")
            
    except np.linalg.LinAlgError:
        print("Error: The matrix is singular. The system does not have a unique solution.")

if __name__ == "__main__":
    solve_system()