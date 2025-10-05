def preprocess_text(text):
    # Function to preprocess the input text
    # This can include lowercasing, removing punctuation, etc.
    return text.lower()

def tokenize_text(text):
    # Function to tokenize the input text into words
    return text.split()

def analyze_sentiment(text):
    # Placeholder function for sentiment analysis
    # In a real implementation, this would use a model to analyze sentiment
    return "Positive" if "good" in text else "Negative"

def extract_entities(text):
    # Placeholder function for entity extraction
    # In a real implementation, this would use a model to extract entities
    return ["Entity1", "Entity2"] if "example" in text else []

# Example usage
if __name__ == "__main__":
    sample_text = "This is a good example."
    preprocessed = preprocess_text(sample_text)
    tokens = tokenize_text(preprocessed)
    sentiment = analyze_sentiment(preprocessed)
    entities = extract_entities(preprocessed)

    print("Tokens:", tokens)
    print("Sentiment:", sentiment)
    print("Entities:", entities)