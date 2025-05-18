def get_num_words(text):
    words = text.split()
    num_words = len(words)
    # return the number of words in the text
    # print(f"{len(words)} words found in the document.")
    return num_words

def get_num_characters(text):
    # Initialize a counter
    count = 0
    # Initialize a dictionary to store character counts
    char_count = {}
    # Loop through each character in the text
    for char in text:
        # take the character and make it lowercase
        char = char.lower()
        # if character is in your dictionary, increment the count
        if char in char_count:
            char_count[char] += 1
        # else add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1

    # return the dictionary
    return char_count

def get_sorted_counts(text):
    # Initialize an empty list to store character counts
    char_list = []
    # Get the character counts dictionary using the get_num_characters function
    char_count = get_num_characters(text)
   
    # Each dictionary should have 2 key-value pairs: 
    # "char" tied to the character and "num" tied to the count value
    # Iterate through the characters and filter out the non-alphabetic characters
    for char, count in char_count.items():
        # Check if the character is alphabetic
        if char.isalpha():
            # Create a dictionary for each character and its count
            char_dict = {"char": char, "num": count}
            # Append the dictionary to the list
            char_list.append(char_dict)
    
    # Sort the list of dictionaries by the count value in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)    

    return char_list