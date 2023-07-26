import math


def calculate_area(blade_length):
    return math.pi * blade_length ** 2


def calculate_power(blade_length, air_density=1.23, wind_velocity=6, power_coeffecient=0.4):
    """Calculates the power of a windmill given the blade_sweep_area.

    NOTE: Maximum allowable wind_velocity = 20 m/s. If greater power = 0.

    Will default to shore values from handout.

    Args:
        blade_length (float): (m) Length of the blade
        air_density (float, optional): (kg/m^3) Defaults to 1.23.
        wind_velocity (float, optional): (m/s). Defaults to 6.
        power_coeffecient (float, optional): (unitless) Defaults to 0.4.

    Returns:
        power: (w) power generated by turbine.
    """

    power = None  # declared for global scope

    max_wind_velocity = 20  # provided by handout
    min_wind_velocity = 4  # provided by handout
    if (wind_velocity > max_wind_velocity):
        print(
            f"ERROR: Wind speeds have exceeded maximum wind velocity [{max_wind_velocity}m/s].\nCutting power to turbine.")
        power = 0
    elif (wind_velocity < min_wind_velocity):
        print(
            f"ERROR: Wind speeds insufficient. Minimum wind velocity [{min_wind_velocity}m/s].\nCutting power to turbine.")
        power = 0
    else:
        blade_sweep_area = calculate_area(blade_length)

        power = 1/2 * air_density * blade_sweep_area * \
            (wind_velocity ** 3) * power_coeffecient
    return power
