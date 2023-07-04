#Sara Umer 1999495 

def strengthen_password(password):
    replacements = {
        'i': '!',
        'a': '@',
        'm': 'M',
        'B': '8',
        'o': '.',
    }
    strengthened_password = ''

    # Replace characters
    for char in password:
        if char.lower() in replacements:
            strengthened_password += replacements[char.lower()]
        else:
            strengthened_password += char
    
    # Append "q*s" to the end
    strengthened_password += 'q*s'
    
    return strengthened_password

# Example usage
simple_password = input()
strong_password = strengthen_password(simple_password)
print(strong_password)
