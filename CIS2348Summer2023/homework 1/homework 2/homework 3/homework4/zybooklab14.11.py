# Sara Umer 1999495
# zybook lab 14.11


# Write the function selection_sort_descend_trace() that takes an integer list and sorts the list into descending order.

# The function should use nested loops and output the list after each iteration of the outer loop, thus outputting the list N-1 times (where N is the size).
def selection_sort_descend_trace(nums):
    n = len(nums)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_index]:
                max_index = j

        # Swap the maximum element with the element at index i
        nums[i], nums[max_index] = nums[max_index], nums[i]

        # Print the current list after this iteration
        print(*nums, end=' ')
        print()  # Move to the next line after printing the sequence


# Complete __main__ to read in a list of integers, and then call selection_sort_descend_trace() to sort the list.
if __name__ == "__main__":
    # Read the list of integers from input
    nums = list(map(int, input().split()))

    # Call the selection_sort_descend_trace() function to sort the list
    selection_sort_descend_trace(nums)

