# Sara Umer 1999495 

# Write a program that gets a list of integers from input, and putputs non-negative integers in ascending order (lowest to highest).


def main():
    # List of numbers
    input_str = input()
    input_list = [int(x) for x in input_str.split()]

    # Filter 
    non_negative_numbers = filter(lambda x: x >= 0, input_list)

    # Sort numbers
    sorted_numbers = sorted(non_negative_numbers)

    # Print the sorted non-negative numbers
    print (*sorted_numbers,"") 
    


if __name__ == "__main__":
    main()
