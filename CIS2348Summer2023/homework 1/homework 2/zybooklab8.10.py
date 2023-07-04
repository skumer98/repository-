# Sara Umer 1999495

def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()

    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# Test inputs "Bob"
input_w = input()

# palindrome
if is_palindrome(input_w):
    print(input_w, "is a palindrome")
else:
    print(input_w, "is not a palindrome")
