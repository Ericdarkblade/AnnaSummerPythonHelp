def Absorb_Calc(path_length, molar_extinction_coefficient, absorbency):
    """
    Calculates the concentration of a solution using Beer's Law:
    A = εcb
    A: absorbency
    ε: molar extinction coefficient of the absorber
    c: concentration
    b: path length

    @param path_length: the path length that light must travel.
    @param molar_extinction_coefficient: coefficient of molar extinction for the given solution.
    @param absorbency: the provided absorbency
    @return concentration: the concentration of the solution
    """
    concentration = absorbency / (molar_extinction_coefficient * path_length)
    return concentration

def parse_data(path_of_data):
    with open(path_of_data, "r") as data_file:
        substance_name = data_file.readline().strip()
        print(f"The name of the substance is {substance_name}.")

        path_length  = float(data_file.readline().strip())
        molar_extinction_coefficient = float(data_file.readline().strip())

        absorbency = data_file.readline().strip()

        while absorbency:
            absorbency = float(absorbency)
            concentration = Absorb_Calc(path_length,molar_extinction_coefficient,absorbency)
            print(f"For {absorbency} absorbancy value, the concentration is {concentration}")
            absorbency = data_file.readline().strip()

parse_data("Py4_Task2_input.txt")