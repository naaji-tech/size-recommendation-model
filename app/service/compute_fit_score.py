from app.utils.config import WEIGHTS


def compute_fit_score(user_meas, garment_meas):
    """
    Compute a weighted fit score between user and garment measurements.
    Lower score indicates a better fit.

    Parameters:
      user_meas (dict): User measurements (e.g., chest, waist, shoulder_width, etc.)
      garment_meas (dict): Garment measurements for a given size.
      weights (dict): Weights assigned to each measurement dimension.

    Returns:
      float: The overall fit score.
    """
    score = 0.0
    for key, weight in WEIGHTS.items():
        # Check if both measurements are available
        if key in user_meas and key in garment_meas:
            diff = abs(user_meas[key] - garment_meas[key])
            score += weight * diff

    return score
