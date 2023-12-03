      #BDD
# Given a sentence
# When the word_frequency function is called with the sentence
# Then the function should return a dictionary containing the frequency of each word
# And punctuation should be ignored
# And words should be considered in a case-insensitive manner


    #pseudocode
# Function word_frequency(sentence):
 #   Initialize an empty dictionary to store word frequencies
 #   Split the sentence into words
 #   For each word in the words:
 #       Remove punctuation and convert to lowercase
 #       If the word is not in the dictionary, add it with a count of 1
 #       If the word is already in the dictionary, increment its count by 1
 #   Return the dictionary of word frequencies



def word_frequency(sentence):
    word_freq = {}
    
    # Split the sentence into words
    words = sentence.split()
    
    for word in words:
        # Remove punctuation and convert to lowercase
        cleaned_word = word.strip(string.punctuation).lower()
        
        # Update word frequency in the dictionary
        if cleaned_word:
            word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1
    
    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
