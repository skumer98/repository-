# Sara Umer 1999495 

# Write a program that calculates an adult's fat-burning heart rate, which is 70% of 220 minus the person's age.

# Complete fat_burning_heart_rate() to calculate the fat burning heart rate.



# The adult's age must be between the ages of 1 and 75. 
# If the age entered is not in this range, raise a ValueError exception in get_age() with the messgae "invalid age." 
# Handle the exception in _main_ and print the ValueError message along with "Could not calculate heart rate info."


def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a", age, "year-old:", heart_rate, "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")


    
   
