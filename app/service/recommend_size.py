from app.service.compute_fit_score import compute_fit_score


def recommend_size(user_measurements: dict, garment_sizes: dict, measurement_weight: dict) -> str:
    """
    Recommend the best garment size based on the lowest fit score.

    Parameters:
        user_measurements (dict): The body measurement values from the user.
        garment_sizes (dict): A mapping of garment size (e.g., 'S', 'M', 'L') to their measurements.

    Returns:
        str: The recommended garment size.
    """

    best_size = None
    best_score = float("inf")

    # Evaluate each garment size
    for size, meas in garment_sizes.items():
        print(f"\nSize {size} measurements: {meas}")
        score = compute_fit_score(user_measurements, meas, measurement_weight)
        # Debug print to show score per size
        print(f"Size {size} has a fit score of {score:.2f}\n")
        if score < best_score:
            best_score = score
            best_size = size

    return best_size
