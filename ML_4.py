# Define the function and its derivative
def function(x):
    return (x + 3) ** 2

def gradient(x):
    return 2 * (x + 3)

# Gradient Descent Implementation
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point  # Starting value of x
    for i in range(iterations):
        grad = gradient(x)  # Compute the gradient
        x = x - learning_rate * grad  # Update x
        print(f"Iteration {i + 1}: x = {x:.4f}, y = {function(x):.4f}")
    return x

# Parameters
starting_point = 2  # Initial value of x
learning_rate = 0.1  # Step size
iterations = 20  # Number of iterations

# Run Gradient Descent
optimal_x = gradient_descent(starting_point, learning_rate, iterations)
print(f"\nLocal minima occurs at x = {optimal_x:.4f}, y = {function(optimal_x):.4f}")
