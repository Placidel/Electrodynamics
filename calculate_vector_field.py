import numpy as np

def calculate_vector_field(gradient, divergence, curl, x, y, z, field_type='gradient'):
    """
    Calculate the gradient, divergence, or curl of a vector field.

    Parameters:
    - gradient: function for the gradient of the field
    - divergence: function for the divergence of the field
    - curl: function for the curl of the field
    - x, y, z: coordinates where the field is evaluated
    - field_type: 'gradient', 'divergence', or 'curl' (default is 'gradient')

    Returns:
    - The result of the selected field calculation
    """
    if field_type == 'gradient':
        return gradient(x, y, z)
    elif field_type == 'divergence':
        return divergence(x, y, z)
    elif field_type == 'curl':
        return curl(x, y, z)
    else:
        raise ValueError("Invalid field_type. Choose 'gradient', 'divergence', or 'curl'.")

# Example usage:

# Define a scalar field for gradient calculation
def scalar_field(x, y, z):
    return x**2 + y**2 + z**2

# Define the gradient of the scalar field
def gradient(x, y, z):
    grad_x = 2 * x
    grad_y = 2 * y
    grad_z = 2 * z
    return np.array([grad_x, grad_y, grad_z])

# Define a vector field for divergence and curl calculation
def vector_field(x, y, z):
    return np.array([x, y, z])

# Define the divergence of the vector field
def divergence(x, y, z):
    div = 1 + 1 + 1  # As the vector field is [x, y, z], the divergence is 1 + 1 + 1
    return div

# Define the curl of the vector field
def curl(x, y, z):
    curl_x = 0
    curl_y = 0
    curl_z = 0
    return np.array([curl_x, curl_y, curl_z])

# Coordinates
x, y, z = 1, 2, 3

# Calculate gradient
print("Gradient:", calculate_vector_field(gradient, divergence, curl, x, y, z, field_type='gradient'))

# Calculate divergence
print("Divergence:", calculate_vector_field(gradient, divergence, curl, x, y, z, field_type='divergence'))

# Calculate curl
print("Curl:", calculate_vector_field(gradient, divergence, curl, x, y, z, field_type='curl'))
