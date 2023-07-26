import math

side_length = 10  #(cm)
height = 15  #(cm)



while True:
    number_of_sides = int(input("Please enter in a value [3-10]\n"))

    if (number_of_sides < 3 or number_of_sides > 10):
        print("Invalid value was entered please enter a legal value")
    else:
        break

area = (number_of_sides * side_length**2) / \
    (4 * math.tan(math.pi / number_of_sides))

volume = area * height

print(f"Area = {area.__round__(3)}\nVolume = {volume.__round__(3)}")