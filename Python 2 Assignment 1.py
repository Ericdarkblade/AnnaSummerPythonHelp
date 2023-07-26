def calculate_hydration(water_mass, flour_mass):
    """Calculates the hydration ratio as water / flour and prints the acceptable range of water mass if calculated hydration ratio is out of bounds.

    Consts:
        lower_hydration_ratio (float) = 0.7
         upper_hydration_ratio (float) = 0.8

    Args:
        water_mass (int): mass of water (g)
        flour_mass (int): mass of flour (g)
    """
    hydration_ratio = water_mass / flour_mass
    lower_hydration_ratio = 0.7
    upper_hydration_ratio = 0.8
    if (hydration_ratio <= upper_hydration_ratio and hydration_ratio >= lower_hydration_ratio):
        print("Hydration falls within range")
    else:
        lower_water_mass = lower_hydration_ratio * flour_mass
        upper_water_mass = upper_hydration_ratio * flour_mass
        print(
            f"Water mass may fall between [{lower_water_mass}g] - [{upper_water_mass}g]")


def calculate_salt_ratio(salt_mass, flour_mass):
    """Calculates the ratio of salt to flour and prints the acceptable range of salt mass if the calculated ratio falls out of bounds.

    Args:
        salt_mass (int): mass of salt (g)
        flour_mass (int): mass of flour (g)
    """
    salt_ratio = salt_mass / flour_mass
    lower_salt_ratio = .01
    upper_salt_ratio = .03
    if (salt_ratio <= upper_salt_ratio and salt_ratio >= lower_salt_ratio):
        print("Salt ammount falls within range")
    else:
        lower_salt_mass = lower_salt_ratio * flour_mass
        upper_salt_mass = upper_salt_ratio * flour_mass
        print(
            f"Salt mass may fall between [{lower_salt_mass}g] - [{upper_salt_mass}g]")


def determine_bake_time(flour_mass):
    # All integer values used for inequalities entered in are mass in grams
    if (flour_mass < 100):
        print("10 minutes")
    elif (flour_mass < 250):
        print("15 minutes")
    elif (flour_mass < 500):
        print("25 minutes")
    elif (flour_mass < 750):
        print("30 minutes")
    elif (flour_mass < 1000):
        print("40 minutes")
    else:
        print(
            f"ERROR: flour mass [{flour_mass}] is too large for factory equipment!")


def calculate_all(flour_mass, water_mass, salt_mass):
    calculate_hydration(water_mass, flour_mass)
    calculate_salt_ratio(salt_mass, flour_mass)
    determine_bake_time(flour_mass)


def test_case_1():
    calculate_all(flour_mass=750, water_mass=600, salt_mass=15)


def test_case_2():
    calculate_all(flour_mass=400, water_mass=100, salt_mass=10)


def live_calculation():
    flour_mass = int(input("Please input flour mass (g): "))
    water_mass = int(input("Please input water mass (g): "))
    salt_mass = int(input("Please input salt mass (g): "))

    calculate_all(flour_mass, water_mass, salt_mass)


print("Test Case 1:")
test_case_1()
print("\n\nTest Case 2:")
test_case_2()


live_calculation()
