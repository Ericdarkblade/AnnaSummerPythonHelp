def calculate_energy(power, time):
    """Calculates the energy output from a heater.

    Args:
        power (float): (w)
        time (int): (s)

    Returns:
        energy (float): (J)
    """

    energy = power * time
    return energy