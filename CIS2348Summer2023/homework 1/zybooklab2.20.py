#Sara Umer 199495 

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print('{:.2f}'.format(your_value))
#(1) Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade. Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size. (Submit for 2 points).

print("Enter amount of lemon juice (in cups):")
lemon_juice = int(input())
print("Enter amount of water (in cups):")
cup_water = int(input())
print("Enter amount of agave nectar (in cups):")
agave_nectar = float(input())
                   
print("How many servings does this make?")
serv_1 = int(input())



print("Lemonade ingredients - yields",'{:.2f}'.format(serv_1),"servings")
print('{:.2f}'.format(lemon_juice),"cup(s) lemon juice")
print('{:.2f}'.format(cup_water),"cup(s) water")
print('{:.2f}'.format(agave_nectar),"cup(s) agave nectar")

print("How many servings would you like to make?")
serv_make = int(input())

print("Lemonade ingredients - yields 48.00 servings")
print('{:.2f}'.format(lemon_juice*8),"cup(s) lemon juice")
print('{:.2f}'.format(cup_water*8),"cup(s) water")
print('{:.2f}'.format(agave_nectar*8),"cup(s) agave nectar")

print("Lemonade ingredients - yields 48.00 servings")
print('{:.2f}'.format(lemon_juice-1),"gallon(s) lemon juice")
print('{:.2f}'.format(cup_water-8),"gallon(s) water")
print('{:.2f}'.format(agave_nectar/2),"gallon(s) agave nectar")
