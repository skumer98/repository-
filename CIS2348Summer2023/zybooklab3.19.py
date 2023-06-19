#Sara Umer 1999495

#(1) Prompt the user to input a wall's height and width. Calculate and output the wall's area (integer). (Submit for 2 points).
print("Enter wall height (feet):")
wall_height = int(input())
print("Enter wall width (feet):")
wall_width = int(input())

print("Wall area:",wall_height*wall_width,"square feet")
wall_area = wall_height*wall_width

#(2) Extend to also calculate and output the amount of paint in gallons needed to paint the wall (floating point). Assume a gallon of paint covers 350 square feet. Store this value in a variable. Output the amount of paint needed using the %f conversion specifier. (Submit for 2 points, so 4 points total).

gal_paint = 350

print("Paint needed:",wall_area/gal_paint,"gallons")

#(3) Extend to also calculate and output the number of 1 gallon cans needed to paint the wall. Hint: Use a math function to round up to the nearest gallon. (Submit for 2 points, so 6 points total).
import math 

print("\nCans needed:",math.ceil(gal_paint/wall_area),"can(s)")

#(4) Extend by prompting the user for a color they want to paint the walls. Calculate and output the total cost of the paint cans depending on which color is chosen. Hint: Use a dictionary to associate each paint color with its respective cost. Red paint costs $35 per gallon can, blue paint costs $25 per gallon can, and green paint costs $23 per gallon can. (Submit for 2 points, so 8 points total).
red = "$35"
blue = "$25"
green = "$23" 


print("Choose a color to paint the wall:")
color = input() 
print("Cost of purchasing red paint:",red)