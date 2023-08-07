# Sara Umer 199495 
# Zybook lab 12.9

# The given program reads a list of single-word first names and ages (ending with -1), and outputs that list with the age incremented. 
# The program fails and throws an exception if the second input on a line is a string rather than an integer. 
#  At FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for the age.

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        # Try to convert the age to an integer
        age = int(parts[1]) + 1
    except ValueError:
        # If ValueError occurs (e.g., when the second input is not an integer), set age to 0
        age = 0

    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
