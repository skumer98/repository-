# Sara Umer 1999495

import csv

# Get name
input_file = input()

# csv.reader()
with open(input_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Create a dictionary 
    word_freq = {}
    
    
    for row in csv_reader:
        # Iterate over each word in the row
        for word in row:
            # Remove spaces and convert to lowercase
            word = word.strip().lower()
            
            # frequency count for the word
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

# Output 
for word, freq in word_freq.items():
    print(word, freq)
