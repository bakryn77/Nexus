from .indexer import load_index # imports load_index function from indexer module
from .embeddings import embed_text # imports embed_text function from embeddings module
import math # imports math module for mathematical functions

def euclidean(v1: list, v2: list) -> float: # defines function to compute euclidean distance
    #euclidean distance is the square root of the sum of the squared differences between corresponding elements of the two vectors
    """
    Compute Euclidean distance between two vectors.
    Lower = more similar.
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2))) #calculate euclidean distance

def search_notes(query: str) -> dict: # defines function to search notes
    """
    Returns the most similar note as a dict with keys: file, text, vector.
    """
    index = load_index() # loads the index
    if not index: # checks if index is empty
        return None # returns None if index is empty

    query_vector = embed_text(query) # embeds the query text

    best_match = None # variable to store best match
    best_distance = float("inf") # variable to store best distance

    for entry in index: # iterates through each entry in the index
        distance = euclidean(query_vector, entry["vector"]) # calculates euclidean distance between query and entry
        if distance < best_distance: # checks if current distance is better than best distance
            best_distance = distance # updates best distance
            best_match = entry # updates best match

    return best_match # returns the best match

def search_top_k(query: str, k: int = 3) -> list:
    """
    Returns the top-k most similar notes.
    """
    index = load_index()
    if not index:
        return []

    query_vector = embed_text(query)

    scored = []
    for entry in index:
        distance = euclidean(query_vector, entry["vector"])
        scored.append((distance, entry))

    scored.sort(key=lambda x: x[0])  # Sort by distance (lower is better)

    return [entry for dist, entry in scored[:k]]  # Return top-k entries