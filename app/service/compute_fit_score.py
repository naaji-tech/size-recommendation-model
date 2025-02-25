from app.utils.config import BODY_GARMENT_SIZE_MAP, CORE_MEASUREMENTS


def compute_fit_score(user_meas: dict, garment_meas: dict, weights: dict) -> float:
    """
    Compute a weighted fit score between user and garment measurements.
    Lower score indicates a better fit.

    Parameters:
        user_meas (dict): User measurements (e.g., chest, waist, shoulder_width, etc.)
        garment_meas (dict): Garment measurements for a given size.

    Returns:
        float: The overall fit score.
    """

    score = float("inf")

    for key, val in BODY_GARMENT_SIZE_MAP.items():
        if key in user_meas and val in garment_meas and garment_meas[val] != 0:
            print(f"User measurement: {key} = {user_meas[key]}")
            print(f"Garment measurement: {val} = {garment_meas[val]}")
            if garment_meas[val] - user_meas[key] < 0 and key in CORE_MEASUREMENTS:
                return float("inf")
            else:
                score = 0.0
            diff = abs(garment_meas[val] - user_meas[key])
            print(f"Diff: {diff}")
            score += weights[val] * diff

    return score
