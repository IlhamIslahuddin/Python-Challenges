import string

def calculate_average_word_length(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Calculate the total length of all the words
    total_length = sum(len(word) for word in words)
    
    # Calculate the number of words
    num_words = len(words)
    
    # Handle the case when there are no words in the file
    if num_words == 0:
        return 0
    
    average_word_length = total_length / num_words
    return average_word_length

if __name__ == "__main__":
    file_path = 'test.txt'  # Replace with the actual file path
    average_length = calculate_average_word_length(file_path)
    print(f"The average word length is: {average_length:.2f}")
