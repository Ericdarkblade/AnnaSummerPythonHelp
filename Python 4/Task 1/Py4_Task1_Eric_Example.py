with open("Py4_Task1_input.txt", "r") as input_text:  # this will automatically close the file
    with open("Py4_Task1_output.txt", "w") as out_text:
        lines_to_read = int(input_text.readline().strip())

        for i in range(lines_to_read):
            line_as_string = input_text.readline().strip()
            out_text.write(line_as_string + '\n')

            # if you wanted to use your own regex you would have to:
            # import re
            # line_as_list = re.split(r"\s+", line_as_string)
            line_as_list = line_as_string.split()  # by default will split by any whitespace
            out_text.write(str(line_as_list) + '\n')

### Example Below

"""
Without using the with keyword you would need to close the file after using:

input_text = open("Py4_Task1_input.txt", "r")

/* Your code here */

input_text.close()

in general it is better to use:
with function as variable
"""
