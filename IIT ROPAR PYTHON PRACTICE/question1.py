#You're given multiple sentences as a list as input and you need to count the 
# occurance number of time each word occurs
# and Finally you need to output the word with the mximum ocurance



def get_most_frequent_word(lines):
    if not lines:
        return "There is no lines"
    
    word_frequency={}

    

    for line in lines:
        cleaned_line=''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in line)
        words=cleaned_line.split()
 
        for word in words:
            if word in word_frequency:
                word_frequency[word]+=1
            else:
                word_frequency[word]=1
    
    if not word_frequency:
        return "No valid word found"
    
    most_frequent_word=''
    max_frequency = 0

    for word,frequency in word_frequency.items():
        if frequency>max_frequency:
            most_frequent_word=word
            max_frequency=frequency
    
    return most_frequent_word





lines=["The quick brown fox jumps over a lazy dog.",
       "The quick brown fox is quick.",
       "Lazy dogs are not quick."]
print(get_most_frequent_word(lines))