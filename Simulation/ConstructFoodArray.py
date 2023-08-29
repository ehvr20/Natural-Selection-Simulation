import numpy as np

def ConstructFoodArray(foodCount, boundaryRadius):
    # Generate random angles (polar coordinates)
    angles = np.random.uniform(0, 2 * np.pi, foodCount)

    # Generate random radii within the boundary radius
    radii = np.random.uniform(
        0.2*boundaryRadius, 0.9*boundaryRadius, foodCount)

    # Convert polar coordinates to Cartesian coordinates
    x_positions = radii * np.cos(angles)
    y_positions = radii * np.sin(angles)

    # Create the foodArray
    foodArray = np.vstack((x_positions, y_positions))

    return foodArray