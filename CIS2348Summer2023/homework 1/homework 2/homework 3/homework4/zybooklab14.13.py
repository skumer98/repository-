# Sara Umer 1999495 
# zybook lab 14.13

# Given code that reads user IDs (until -1), complete the quicksort() and partition() functions to sort the IDs in ascending order using the Quicksort algorithm.
# Increment the global variable num_calls in quicksort() to keep track of how many times quicksort() is called. 
# The given code outputs num_calls followed by the sorted IDs.

# Global variable
num_calls = 0

# Partitioning algorithm
def partition(user_ids, i, k):
    global num_calls
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]
    done = False
    l = i
    h = k
    while not done:
        while user_ids[l] < pivot:
            l = l + 1
        while pivot < user_ids[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            # Swap user_ids[l] and user_ids[h]
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
    return h

# Quicksort algorithm
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    j = 0
    if i >= k:
        return
    j = partition(user_ids, i, k)
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)


