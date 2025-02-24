from app.service import compute_fit_score


def recommend_size(user_measurements, garment_sizes):
    """
    Recommend the best garment size based on the lowest fit score.

    Parameters:
      user_measurements (dict): The body measurement values from the user.
      garment_sizes (dict): A mapping of garment size (e.g., 'S', 'M', 'L') to their measurements.

    Returns:
      str: The recommended garment size.
    """
    # Define weights for each measurement.
    # Adjust these based on the importance of each measurement.

    best_size = None
    best_score = float("inf")

    # Evaluate each garment size
    for size, meas in garment_sizes.items():
        score = compute_fit_score(user_measurements, meas)
        # Debug print to show score per size
        print(f"Size {size} has a fit score of {score:.2f}")
        if score < best_score:
            best_score = score
            best_size = size

    return best_size
