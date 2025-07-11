import string
from collections import Counter
import matplotlib.pyplot as plt

def clean_text(text):
    # Convert to lowercase and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)

def get_word_frequencies(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    return Counter(words)

def visualize_frequencies(freq_dict):
    # Get the top 5 words
    top = freq_dict.most_common(5)
    words = [item[0] for item in top]
    counts = [item[1] for item in top]

    # Plotting the bar chart
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 5 Most Frequent Words')
    plt.show()

paragraph = input("Enter a paragraph: ")
frequencies = get_word_frequencies(paragraph)

print("\nTop 5 Most Frequent Words:")
for word, count in frequencies.most_common(5):
    print(f"{word}: {count}")

# Bonus: Visualize with bar chart
visualize_frequencies(frequencies)
