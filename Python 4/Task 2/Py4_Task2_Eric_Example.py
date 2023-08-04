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
    """
    Opens a text file:
    Reads the first line of text as the Substance Name (String)
    Reads the second line of text as the Path Length (Float)
    Reads the third line of text as the Molar Extinction Coefficient (Float)

    And iterates through the remaining text document parsing through each absorbency (float)
    and prints a formatted string of the absorbency and calculated concentration.
    @param path_of_data (string): path to the text file to be opened.
    @return None: Prints the calculated concentrations per absorbency in text file.
    """
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