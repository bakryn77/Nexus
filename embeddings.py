import re #re= regular expression module for string matching

def clean_text(text: str) -> str:
    """Lowercase + remove non-letter characters"""""
    text = text.lower() # Convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text) # Remove non-letter characters
    text = " ".join(text.split()) # Remove extra whitespace
    return text

def embed_text(text: str) -> list:
    """
    Convert text into a simple numeric vector.
    (This is a fake embedding for demonstration purposes.)
    """
    text = clean_text(text) #step 1 clean the text
    words = text.split() #step 2 split text into words

    if not words:
        return [0.0]

    numbers = [float(len(w)) for w in words] #convert each word to a number
    avg = sum(numbers) / len(numbers) #calculate average and vector

    return [avg] #return as a vector

