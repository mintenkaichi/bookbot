letters = {}
chars_list = []

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
  
    
def string_counts(text):
    for word in text:
        for letter in word.lower():
            try:
                letters[letter] += 1
            except KeyError:
                letters[letter] = 1
    

def generate_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    chars_list = [(k,v) for k,v in letters.items() if k.isalpha()]
    chars_list.sort(key=lambda x: x[1])
    chars_list.reverse()
    for item in chars_list:
        print(f"The {item[0]} character was found {item[1]} times")

  
string_counts(file_contents)
generate_report()        
