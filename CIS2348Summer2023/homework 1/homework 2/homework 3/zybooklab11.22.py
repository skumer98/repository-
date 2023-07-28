# Sara Umer 1999495 

# write a progeam that reads a list of words. 
# then, the program outputs those words and their frequencies 

#print(input())

#def list_of_words(self):
    #hey = "1", 
    #hi = "2",
    #Mark = "1"
    #hi = "2"
    #mark = "1"

#def list_of_words(self): (input())
#print (input())
def main(): 
    list_of_words = input().split()
    word_list = {}

    for word in list_of_words: 
        word_list[word] = word_list.get(word, 0)+ 1 

    for word, list in word_list.items():
        print(word, list)

if __name__ == "__main__": 
    main() 
