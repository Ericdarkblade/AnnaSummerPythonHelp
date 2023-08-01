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

