from stats import *
import sys

arguments = sys.argv
if len(arguments) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filename = arguments[1]



def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def get_book_report(text, filepath):
    # Assign the book file name to a variable
    book_file = filepath
    # Initialize an empty string to store the report
    report = ""
    # Get the word count using the get_num_words function
    word_count = get_num_words(text)
    # Get the character counts dictionary using the get_num_characters function
    char_count = get_num_characters(text)
    # Get the sorted character counts using the get_sorted_counts function
    char_list = get_sorted_counts(text)

      # Begin the report string template with the header
    report += f"============ BOOKBOT ============\n"
    
    # Print command showing the text file name used to the terminal
    report += f"Analyzing book found at {book_file}...\n"
    
    # Print the total number of words in the book to the terminal
    report += f"----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    
    # Print each tuple in the character list in the format "{char}: {num}"
    report += f"--------- Character Count -------\n"
    for char_dict in char_list:
        report += f"{char_dict['char']}: {char_dict['num']}\n"
    
    # Print the footer to the terminal
    report += f"============= END ===============\n"
    # Return the report string
    return report

def main():
    text = get_book_text(filename)
    report = get_book_report(text, filename)
    print(report)


if __name__ == "__main__":
    main()