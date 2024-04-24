from collections import Counter
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print("File not found.")
        return None

def remove_stopwords(text):
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

def count_word_frequency(words):
    word_counts = Counter(words)
    return word_counts

  
def display_word_frequency(word_counts):
    for word, count in word_counts.items():
        print(f'{word}: {count}')

def main():
    file_path ="paragraphs.txt"
    contents = read_file(file_path)
    
    if contents:
        print("Original text:")
        print(contents)
        
        print("\nText with stopwords removed:")
        processed_text = remove_stopwords(contents)
        print(" ".join(processed_text))  
        
        print("\nWord frequency count:")
        word_counts = count_word_frequency(processed_text)
        display_word_frequency(word_counts)

if __name__ == '__main__':
    main()