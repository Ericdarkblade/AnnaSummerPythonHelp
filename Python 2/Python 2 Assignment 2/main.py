import heater
import wind_turbine

time = 2  # hours
time *= 3600  # seconds

length = 50  # meters
air_density = 1.23  # kg/m^3
velocity = 6  # m/s
power_coeffecient = 0.4  # unitless


print("Wind Power Generation:")
print("-------------------------------------")
print("Using default Values")
power = wind_turbine.calculate_power(length)
print(power)

print()

print("Without using default values")
power = wind_turbine.calculate_power(
    length, air_density, velocity, power_coeffecient)
print(power)
print("-------------------------------------")

print()
print("Heater Energy Calculation")
print("-------------------------------------")
print(heater.calculate_energy(power, time))
print("-------------------------------------")
